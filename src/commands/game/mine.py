import random
import time

from mubble import Dispatch, CallbackQuery
from mubble.rules import CallbackData, CallbackDataMarkup
from mubble.tools import ParseMode

from src.database import User, Ores
from src.keyboards import game_mining_menu

dp = Dispatch()


CHANCES = {
        "stone": 0.80,
        "iron": 0.10,
        "gold": 0.05,
        "diamond": 0.02,
        "void": 0.01,
    }
keys = list(CHANCES.keys())
values = list(CHANCES.values())

EMOJIES = {
    "stone": "⚫️ Камінь",
    "iron": "⚪️ Залізо",
    "gold": "🟡 Золото",
    "diamond": "🟣 Діаманти",
    "void": "🔵 Безкінечність"
}

@dp.callback_query(CallbackData("game_mining"))
async def get_ore_handler(cq: CallbackQuery, user: User):
    ores: Ores = await user.ores.first()

    text = (
        "💎 <b>Ви зараз в меню добутку руди</b>\n"
        "Список ваших руд:\n"
        "<blockquote>"
        f"⚫️ Камінь: {ores.stone}\n"
        f"⚪️ Залізо: {ores.iron}\n"
        f"🟡 Золото: {ores.gold}\n"
        f"🟣 Діаманти: {ores.diamond}\n"
        f"🔵 Безкінечність: {ores.void}\n"
        "</blockquote>\n"
    )
    await cq.edit_text(
        text,
        parse_mode=ParseMode.HTML,
        reply_markup=game_mining_menu
    )


@dp.callback_query(CallbackData("start_mining"))
async def start_mining_handler(cq: CallbackQuery, user: User):
    if not user.workers:
        await cq.answer("💎 Ви не маєте робітників!")
        return
    
    if user.mining_timestamp != 0:
        await cq.answer("💎 Ви вже почали добуток руди!")
        return
    user.mining_timestamp = time.time()
    await user.save()
    await cq.answer("💎 Ви почали добуток руди!")


@dp.callback_query(CallbackData("end_mining"))
async def end_mining_handler(cq: CallbackQuery, user: User):
    if user.mining_timestamp == 0:
        await cq.answer("💎 Ви не почали добуток руди!")
        return

    time_difference = round((time.time() - user.mining_timestamp) / 10)
    if time_difference == 0:
        await cq.answer("💎 Ви ще не добули жодної руди!")

    elif time_difference > 60:
        amounts = random.choices(keys, weights=values, k=60)
        await cq.answer("💎 Ви не можете добувати руду більше ніж 1 годину.")
    else:
        amounts = random.choices(keys, weights=values, k=time_difference)

    ores: Ores = await user.ores.first()

    results = {amount: amounts.count(amount) for amount in set(amounts)}

    ores.stone += results.get("stone", 0)
    ores.iron += results.get("iron", 0)
    ores.gold += results.get("gold", 0)
    ores.diamond += results.get("diamond", 0)
    ores.void += results.get("void", 0)

    user.mining_timestamp = 0
    await ores.save()
    await user.save()

    new_ores = ""
    for key, value in results.items():
        new_ores += f"{EMOJIES.get(key, '')}: {value}\n"

    text = (
        "💎 <b>Ви зараз в меню добутку руди</b>\n"
        "Список ваших руд:\n"
        "<blockquote>"
        f"⚫️ Камінь: {ores.stone}\n"
        f"⚪️ Залізо: {ores.iron}\n"
        f"🟡 Золото: {ores.gold}\n"
        f"🟣 Діаманти: {ores.diamond}\n"
        f"🔵 Безкінечність: {ores.void}\n"
        "</blockquote>\n"
        "За минулу сесію ви добули:\n"
        "<blockquote>"
        f"{new_ores}"
        "</blockquote>"
    )

    await cq.edit_text(text, parse_mode=ParseMode.HTML, reply_markup=game_mining_menu)
    await cq.answer(f"💎 Ви завершили добуток руди!")
