from mubble import Dispatch, CallbackQuery
from mubble.rules import CallbackData
from mubble.tools import ParseMode

from src.database import User
from src.keyboards import game_menu

dp = Dispatch()


@dp.callback_query(CallbackData("game"))
async def menu_handler(cq: CallbackQuery, user: User):
    text = (
        f"⛰ <b> {user.nickname}, вітаємо вас в меню гри!</b>\n"
    )
    await cq.edit_text(
        text,
        parse_mode=ParseMode.HTML,
        reply_markup=game_menu
    )
