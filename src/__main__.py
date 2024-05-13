from mubble import Token, API, Dispatch, Mubble
from tortoise import Tortoise

from src import dps

api = API(Token.from_env(path_to_envfile=".env"))
dispatch = Dispatch()

for dp in dps:
    dispatch.load(dp)

bot = Mubble(api, dispatch=dispatch)


async def setup_database():
    await Tortoise.init(
        db_url="sqlite://database.sqlite3",
        modules={"models": ["src.database.user", "src.database.ores"]}
    )
    await Tortoise.generate_schemas()
    Tortoise.init_models(["src.database.user", "src.database.ores"], "models")
    print("Database setup complete!")

bot.loop_wrapper.add_task(setup_database())
bot.run_forever()
