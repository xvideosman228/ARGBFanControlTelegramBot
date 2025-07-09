from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.types import Message

from keyboard import customPresetsKeyboard, colorKeyboard, timeKeyboard
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
async def colorPick(message: Message, state: FSMContext):
    colorIndex = int(list(names["colors"]["basicColors"].values()).index(message.text))
    color = list(names["colors"]["basicColors"].keys())[colorIndex]
    logger.info(f"Выбран {color.capitalize()} для Fade In / Out")
    await state.update_data(COLOR_FADE_IN_OUT=f"{color.upper()}")
    await state.set_state(StateMachine.TIME_FADE_IN_OUT)
    await message.answer(names["colors"]["basicColors"][f"{color}"] + ' для ' + names["custom"]["fadeinout"], reply_markup=timeKeyboard)

@exception
@fadeInOutRouter.message(StateFilter(StateMachine.TIME_FADE_IN_OUT), F.text.in_(names["times"].values()))
async def timePick(message: Message, state: FSMContext):
    timeIndex = int(list(names["times"].values()).index(message.text))
    time = list(names["times"].keys())[timeIndex]
    logger.info(f"Выбран {time} для Color Wipe 2")

    await message.answer(names["times"][f"{time}"] + ' установлено в качестве времени для ' + (names["custom"]["fadeinout"]))
    color = await state.get_data()
    await state.set_state(StateMachine.CUSTOM_PRESETS)
    FanController.fadeinout(f'{color["COLOR_FADE_IN_OUT"]}', f'{time.upper()}')

"""
    "fire": "\uD83D\uDD25 огонь",
    "ocean": "\uD83C\uDF0A океан"
"""