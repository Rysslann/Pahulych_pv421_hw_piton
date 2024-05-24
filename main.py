import asyncio
import logging
import sys
from creds import main

# init
dp = main.dp
bot = main.bot


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
