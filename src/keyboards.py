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
    .add(InlineButton("🏬 Продати руду", callback_data="game_sell"))
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

game_sell_menu = (
    InlineKeyboard()
    .add(InlineButton("🛒 Продати руду вибірково", callback_data="sell_particular"))
    .row()
    .add(InlineButton("🛍 Продати всю руду", callback_data="sell_all"))
    .row()
    .add(InlineButton("⬅️ Back", callback_data="game"))
).get_markup()

sell_particular_menu = (
    InlineKeyboard()
    .add(InlineButton("⚫️ Продати весь камінь", callback_data="sell_stone"))
    .add(InlineButton("⚪️ Продати все залізо", callback_data="sell_iron"))
    .add(InlineButton("🟡 Продати все золото", callback_data="sell_gold"))
    .add(InlineButton("🟣 Продати всі діаманти", callback_data="sell_diamond"))
    .add(InlineButton("🔵 Продати всю безкінечність", callback_data="sell_void"))
    .row()
    .add(InlineButton("⬅️ Back", callback_data="game"))
).get_markup()
