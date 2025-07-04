import logging.config
import json
from functools import wraps

with open('config/loggerConfig.json') as conf:
    logConfig = json.load(conf)


logging.config.dictConfig(logConfig)
logger = logging.getLogger('logger')


def exception(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            await func(*args, **kwargs)
        except Exception:
            err = f"There is an exception in {func.__name__}"
            logger.exception(err)
    return wrapper