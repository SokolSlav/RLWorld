import random
import time

from mubble import Token, API, Mubble, Message
from mubble.rules import StartCommand, Command, Markup

api = API(Token.from_env(path_to_envfile=".env"))
bot = Mubble(api)


def get_random_emoji() -> str:
    """
    Returns a random emoji
    """
    emojis_list = ["🐷", "🦊", "🙉", "🦓", "🐸", "🐼"]
    return random.choice(emojis_list)


@bot.on.message(StartCommand())
async def start(message: Message):
    await message.answer(
        f"{get_random_emoji()} Привіт, {message.from_user.first_name}!\n"
        "Список моїх команд:\n"
        "/time_now - Подивитися час\n"
        "/repeat"
    )


@bot.on.message(Command("time_now"))
async def time_now(message: Message):
    time_now = time.strftime("%H:%M:%S")
    await message.answer(f"{get_random_emoji()} Теперішній час: {time_now}")


@bot.on.message(Markup(["/repeat", "/repeat <text>"]))
async def answer(message: Message, text: str = None):
    if text is None:
        await message.reply(
            f"{get_random_emoji()} Ви забули вказати текст.\n"
            "Приклад: /repeat Привіт! Як справи?"
        )
        return
    await message.reply(f"{get_random_emoji()} Ваш текст «{text}»")


bot.run_forever()