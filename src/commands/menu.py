from mubble import Dispatch, Message, CallbackQuery
from mubble.rules import StartCommand, CallbackData

from src.database import User
from src.keyboards import menu

dp = Dispatch()


@dp.message(StartCommand())
async def start_handler(message: Message):
    await message.answer(
        "🏕 Твоє <b>меню</b> відкрито!",
        parse_mode="HTML",
        reply_markup=menu
    )

@dp.callback_query(CallbackData("menu"))
async def back_to_menu(cq: CallbackQuery):
    await cq.edit_text(
        "🏕 Твоє <b>меню</b> відкрито!",
        parse_mode="HTML",
        reply_markup=menu
    )