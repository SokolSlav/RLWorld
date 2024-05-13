from mubble import Dispatch, CallbackQuery
from mubble.rules import CallbackData

from src.database import User, Ores
from src.keyboards import back_to_menu

dp = Dispatch()


@dp.callback_query(CallbackData("profile"))
async def profile_handler(cq: CallbackQuery):
    user = await User.get(uid=cq.from_user.id)
    ores: Ores = await user.ores.first()

    await cq.answer("👔 Тут ви можете побачити свою статистику")

    text = (
        f"👔 <b>{user.nickname}</b>, ваш профіль:\n"
        f"💵 Ваш баланс: <b>${user.balance:,d}</b>\n"
        f"Локація: {user.location_text}\n"
        "👷🏽 <b>Інформація про робітників</b>:\n"
        f"• Кількість: <b>{user.workers_count}</b>\n"
        f"• Множник: х1\n\n"
        "💎 <b>Список ваших руд</b>:\n"
        f"⚫️ Камінь: {ores.stone}\n"
        f"⚪️ Залізо: {ores.iron}\n"
        f"🟡 Золото: {ores.gold}\n"
        f"🟣 Діаманти: {ores.diamond}\n"
        f"🔵 Безкінечність: {ores.void}\n"
        
    )
    await cq.edit_text(text, parse_mode="HTML", reply_markup=back_to_menu)
    
