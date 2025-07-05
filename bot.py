from config.botConfig import bot, dp
from config.loggingConfig import logger
from handlers.startMenuHandler import startMenuRouter

dp.include_router(startMenuRouter)

if __name__ == '__main__':
    logger.info("Бот запущен!")
    dp.run_polling(bot)
    logger.info("Бот остановлен!")

