from mubble import InlineKeyboard, InlineButton

menu = (
    InlineKeyboard()
    .add(InlineButton("👔 Профіль", callback_data="profile"))
    .add(InlineButton("⚙️ Налаштування", callback_data="settings"))
    .row()
    .add(InlineButton("⛰ Перейти до гри!", callback_data="game"))
).get_markup()

game_menu = (
    InlineKeyboard()
    .add(InlineButton("👷🏽 Меню робітників", callback_data="game_hire"))
    .row()
    .add(InlineButton("⛏️ Добуток руди", callback_data="game_mining"))
    .add(InlineButton("⬅️ Back", callback_data="menu"))
).get_markup()

game_hire_menu = (
    InlineKeyboard()
    .add(InlineButton("👷🏽 1", callback_data="game_hire_1"))
    .add(InlineButton("👷🏽 5", callback_data="game_hire_5"))
    .add(InlineButton("👷🏽 10", callback_data="game_hire_10"))
    .row()
    .add(InlineButton("⬅️ Back", callback_data="game"))
).get_markup()

game_mining_menu = (
    InlineKeyboard()
    .add(InlineButton("🟢 Почати добуток", callback_data="start_mining"))
    .add(InlineButton("🔴 Зупинити добуток", callback_data="end_mining"))
    .row()
    .add(InlineButton("⬅️ Back", callback_data="game"))
).get_markup()

back_to_menu = (
    InlineKeyboard()
    .add(InlineButton("⬅️ Back", callback_data="menu"))
).get_markup()

