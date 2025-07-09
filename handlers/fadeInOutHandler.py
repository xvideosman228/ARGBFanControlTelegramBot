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
@fadeInOutRouter.message(StateFilter(StateMachine.FADE_IN_OUT), F.text.in_(names["colors"]["basicColors"].values()))
async def colorPick(message: Message):
    colorIndex = int(list(names["colors"]["basicColors"].values()).index(message.text))
    color = list(names["colors"]["basicColors"].keys())[colorIndex]
    logger.info(f"Выбран {color.capitalize()} для Fade In / Out")
    await message.answer(names["colors"]["basicColors"][f"{color}"] + ' для ' + names["custom"]["fadeinout"])
    FanController.fadeinout(f'{color.upper()}')



"""
    "fire": "\uD83D\uDD25 огонь",
    "ocean": "\uD83C\uDF0A океан"
"""