from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.types import Message

from keyboard import customPresetsKeyboard, colorKeyboard
from serialControl import FanController
from stateMachine import StateMachine
from config.loggingConfig import exception, logger
import json

with open('./config/buttons.json') as file:
    names = json.load(file)

with open('./config/texts.json') as file:
    texts = json.load(file)

fadeInOutRouter = Router()


@exception
@fadeInOutRouter.message(StateFilter(StateMachine.FADE_IN_OUT), F.text == names["colors"]["basicColors"]["red"])
async def red(message: Message):
    logger.info("Выбран Red для Fade In / Out")
    await message.answer(f'{names["colors"]["basicColors"]["red"]} для {names["custom"]["fadeinout"]}')
    FanController.fadeinout('RED')


@exception
@fadeInOutRouter.message(StateFilter(StateMachine.FADE_IN_OUT))
async def colorChoose(message: Message, state: FSMContext):
    logger.info("Открыто меню выбора цвета для Fade in / out")
    await message.answer(texts["chooseColor"], reply_markup=colorKeyboard)


"""
    "fire": "\uD83D\uDD25 огонь",
    "ocean": "\uD83C\uDF0A океан"
"""