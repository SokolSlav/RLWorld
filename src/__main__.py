from mubble import Token, API, Mubble, Message
from mubble.rules import StartCommand, Command

api = API(Token.from_env(path_to_envfile=".env"))
bot = Mubble(api)


@bot.on.message(StartCommand())
async def start(message: Message):
    await message.answer("Hello world!")
    await message.answer(f"{message}")

bot.run_forever()