from aiogram.filters import StateFilter, or_f
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from keyboard import backKeyboard
from aiogram.types import Message

from stateMachine import StateMachine
from config.loggingConfig import exception, logger
import json

with open('../config/buttons.json') as file:
    names = json.load(file)

with open('../config/texts.json') as file:
    texts = json.load(file)

startStates = (StateMachine.FAN_CONFIG, StateMachine.ABOUT)

startMenuRouter = Router()


@exception
@startMenuRouter.message(StateFilter(StateMachine.START), F.text == names["fanConfig"])
async def fanConfig(message: Message, state: FSMContext):
    logger.info("Кнопка Fan Config нажата")
    await state.set_state(StateMachine.FAN_CONFIG)
    await message.answer(texts["fanConfig"], reply_markup=fanConfigKeyboard)

@exception
@startMenuRouter.message(StateFilter(StateMachine.START), F.text == names["about"])
async def about(message: Message, state: FSMContext):
    logger.info("Кнопка About нажата")
    await state.set_state(StateMachine.ABOUT)
    await message.answer(texts["about"], reply_markup=backKeyboard)

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

