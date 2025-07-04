from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram import F, Router
from aiogram.types import Message
from loggingConfig import exception

startMenuRouter = Router()

@exception
@startMenuRouter.message(Command('start'))
async def start(message: Message):
    await message.answer(f"fw")

