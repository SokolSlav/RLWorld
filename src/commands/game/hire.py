from mubble import Dispatch, CallbackQuery
from mubble.rules import CallbackData, CallbackDataMarkup
from mubble.tools import ParseMode

from src.database import User
from src.keyboards import game_hire_menu

dp = Dispatch()

EMPLOYEE_PRICE = 100



@dp.callback_query(CallbackData("game_hire"))
async def hire_menu_handler(cq: CallbackQuery, user: User):
    text = (
        "👷🏽 Оберіть кількість робітників\n"
        f"- Зараз у вас: {user.workers_count}"
    )
    
    await cq.edit_text(
        text=text,
        reply_markup=game_hire_menu
    )


@dp.callback_query(CallbackDataMarkup("game_hire_<number:int>"))
async def hire_handler(cq: CallbackQuery, user: User, number: int):
    price = EMPLOYEE_PRICE * number

    if user.balance < price:
        await cq.answer(f"💵 Вам не вистачає: ${price - user.balance}")
        return

    user.balance -= price

    for _ in range(number):
        user.workers.append(
            {
                "level": 1,
                "exp": 0,
                "exp_need": 100,
                "multiplier": 0
            }
        )
        
    await user.save()
    await cq.answer(f"👷🏽 Тепер у вас {user.workers_count} робітників!")
