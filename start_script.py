from core import settings
from log import setup_logger

from database.settings import database_manager


async def main():
    # only if you use without docker!
    # from dotenv import load_dotenv
    # load_dotenv("../local.env")

    setup_logger()
    await database_manager.init()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
