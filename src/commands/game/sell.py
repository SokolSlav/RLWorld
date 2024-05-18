from mubble import Dispatch, CallbackQuery
from mubble.rules import CallbackData, CallbackDataMarkup
from mubble.tools import ParseMode

from src.database import User, Ores
from src.keyboards import game_mining_menu

dp = Dispatch()

PRICES = {
    "stone": 0.3,
    "iron": 1.0,
    "gold": 5.0,
    "diamond": 100.0,
    "void": 1000.0
}


@dp.callback_query(CallbackDataMarkup("sell_<type_>"))
async def sell_ore_by_type(cq: CallbackQuery, user: User, type_: str):
    ores: Ores = await user.ores.first()
    amount = round(PRICES[type_] * ores.raw_counts[type_], 2)
    # for ore_name, ore_count in ores.raw_counts.items():
    #     amount += round(PRICES[ore_name] * ore_count, 2)

    await cq.answer(f"Ви успішно продали {type_} за {amount}")




