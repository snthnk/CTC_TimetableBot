import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config_data.config import Config, load_config
import user_handlers

config = load_config('config_data/.env')
logger = logging.getLogger(__name__)

async def main():
    config: Config = load_config('config_data/.env')
    bot = Bot(token=config.tg_bot.token)
    storage = MemoryStorage()

    dp = Dispatcher(storage=storage)

    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    dp.include_router(user_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
