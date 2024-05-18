from mubble import Dispatch, Message, CallbackQuery, ABCMiddleware
from mubble.bot import Context

from src.database import User, Ores

dp = Dispatch()


@dp.callback_query.register_middleware()
class CallbackWorkers(ABCMiddleware[CallbackQuery]):
    async def pre(self, cq: CallbackQuery, ctx: Context) -> bool:
        user = await User.get(uid=cq.from_user.id)
        for worker in user.workers:
            while worker["exp"] >= worker["exp_need"]:
                worker["exp"] -= worker["exp_need"]
                worker["level"] += 1
                worker["exp_need"] += worker["level"] * worker["exp_need"] // 10
                worker["multiplier"] += 0.025
            await user.save()
        return True
