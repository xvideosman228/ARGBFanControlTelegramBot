from aiogram.filters import StateFilter, or_f
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram import Router, F
from aiogram.types import Message
from keyboard import startKeyboard, backKeyboard
from stateMachine import StateMachine
from config.loggingConfig import exception, logger
import json

with open('./config/buttons.json') as file:
    names = json.load(file)

with open('./config/texts.json') as file:
    texts = json.load(file)

startStates = (StateMachine.FAN_CONFIG, StateMachine.ABOUT)

startMenuRouter = Router()

@exception
@startMenuRouter.message(Command('start'))
async def start(message: Message, state: FSMContext):
    await state.set_state(StateMachine.START)
    await message.answer(texts["start"], reply_markup=startKeyboard)

@exception
@startMenuRouter.message(StateFilter(StateMachine.START), F.text == names["about"])
async def about(message: Message, state: FSMContext):
    logger.info("Кнопка About нажата")
    await state.set_state(StateMachine.ABOUT)
    await message.answer(texts["about"], reply_markup=backKeyboard)

@exception
@startMenuRouter.message(StateFilter(StateMachine.START), F.text == names["startButtons"]["strength+"])
async def strengthplus(message: Message):
    logger.info("Кнопка Strength + нажата")
    await message.answer(texts["strength+"])

@exception
@startMenuRouter.message(StateFilter(StateMachine.START), F.text == names["startButtons"]["strength-"])
async def strengthminus(message: Message):
    logger.info("Кнопка Strength - нажата")
    await message.answer(texts["strength-"])

@exception
@startMenuRouter.message(StateFilter(StateMachine.START), F.text == names["startButtons"]["strength++"])
async def strengthplusplus(message: Message):
    logger.info("Кнопка Strength ++ нажата")
    await message.answer(texts["strength++"])

@exception
@startMenuRouter.message(StateFilter(StateMachine.START), F.text == names["startButtons"]["strength--"])
async def strengthminusminus(message: Message):
    logger.info("Кнопка Strength -- нажата")
    await message.answer(texts["strength--"])

@exception
@startMenuRouter.message(StateFilter(StateMachine.START), F.text == names["startButtons"]["brightness+"])
async def brightnessplus(message: Message):
    logger.info("Кнопка Brightness + нажата")
    await message.answer(texts["brightness+"])

@exception
@startMenuRouter.message(StateFilter(StateMachine.START), F.text == names["startButtons"]["brightness-"])
async def brightnessminus(message: Message):
    logger.info("Кнопка Brightness - нажата")
    await message.answer(texts["brightness-"])

@exception
@startMenuRouter.message(StateFilter(StateMachine.START), F.text == names["startButtons"]["brightness++"])
async def brightnessplusplus(message: Message):
    logger.info("Кнопка Brightness ++ нажата")
    await message.answer(texts["brightness++"])

@exception
@startMenuRouter.message(StateFilter(StateMachine.START), F.text == names["startButtons"]["brightness--"])
async def brightnessminusminus(message: Message):
    logger.info("Кнопка Brightness -- нажата")
    await message.answer(texts["brightness--"])











@exception
@startMenuRouter.message(or_f(*startStates), F.text == names["back"])
async def back(message: Message, state: FSMContext):
    await state.set_state(StateMachine.START)
    await message.answer(texts['start'], reply_markup=startKeyboard)

@exception
@startMenuRouter.message(StateFilter(StateMachine.START), F.text)
async def default(message: Message, state: FSMContext):
    logger.info(f"Пользователь {message.from_user.id} чёто непонятное сказал")
    await state.set_state(StateMachine.START)
    await message.answer(texts['iDidNotFuckingUnderstandYouStupidMoron'], reply_markup=startKeyboard)

