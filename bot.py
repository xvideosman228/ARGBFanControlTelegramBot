from botConfig import bot, dp
# from selectLanguageHandler import selectLanguageRouter
from loggingConfig import logger
from startMenuHandler import startMenuRouter

dp.include_router(startMenuRouter)

if __name__ == '__main__':
    logger.info("Polling has started!")
    dp.run_polling(bot)

    logger.info("Polling has stopped!")

