from aiogram import Bot, Dispatcher
from dotenv import dotenv_values
from aiogram.fsm.storage.redis import RedisStorage


config = dotenv_values('./config/.env')
TOKEN = config['TOKEN']

bot = Bot(token=TOKEN)
storage = RedisStorage.from_url('redis://localhost:6379/0')
dp = Dispatcher(storage=storage)