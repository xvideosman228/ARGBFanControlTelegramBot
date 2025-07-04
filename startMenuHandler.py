from aiogram.filters import StateFilter, or_f
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram import Router, F
from aiogram.types import Message
from keyboard import startKeyboard, backKeyboard
from stateMachine import StateMachine
from config.loggingConfig import exception, logger
import json
from serialControl import button1, button2

with open('config/buttons.json') as file:
    names = json.load(file)

startStates = (StateMachine.STATE1, StateMachine.STATE2)

startMenuRouter = Router()

@exception
@startMenuRouter.message(Command('start'))
async def start(message: Message, state: FSMContext):
    await state.set_state(StateMachine.START)
    await message.answer(f"fw", reply_markup=startKeyboard)

@exception
@startMenuRouter.message(StateFilter(StateMachine.START), F.text == names["button1"])
async def b1(message: Message, state: FSMContext):
    logger.info("Кнопка 1")
    button1()
    await state.set_state(StateMachine.STATE1)
    await message.answer(f"button1", reply_markup=backKeyboard)

@exception
@startMenuRouter.message(StateFilter(StateMachine.START), F.text == names["button2"])
async def b2(message: Message, state: FSMContext):
    logger.info("Кнопка 2")
    button2()
    await state.set_state(StateMachine.STATE2)
    await message.answer(f"button2", reply_markup=backKeyboard)

@exception
@startMenuRouter.message(or_f(*startStates), F.text == names["back"])
async def back(message: Message, state: FSMContext):
    logger.info("Назад в стартовое меню")
    await state.set_state(StateMachine.START)
    await message.answer(f"Back", reply_markup=startKeyboard)

