from mubble import Dispatch, Message, CallbackQuery, ABCMiddleware
from mubble.bot import Context

from src.database import User, Ores


dp = Dispatch()


@dp.message.register_middleware()
class MessageContext(ABCMiddleware[Message]):
    async def pre(self, message: Message, ctx: Context) -> bool:
        user = await User.get_or_none(uid=message.from_user.id)

        if user is None:
            ores = await Ores.create()
            user = await User.create(uid=message.from_user.id, nickname=message.from_user.first_name, ores=ores)

            await message.answer(
                "⛰ Вітаємо вас в <b>RLWorld</b>\n\n"
                "⛏ <b>Добувай, продавай та прокачуй!</b>",
                parse_mode="HTML"
            )

        ctx.set("user", user)
        return True


@dp.callback_query.register_middleware()
class CallbackContext(ABCMiddleware[CallbackQuery]):
    async def pre(self, cq: CallbackQuery, ctx: Context) -> bool:
        user = await User.get_or_none(uid=cq.from_user.id)

        if user is None:
            ores = await Ores.create()
            user = await User.create(uid=cq.from_user.id, nickname=cq.from_user.first_name, ores=ores)

        ctx.set("user", user)
        return True
