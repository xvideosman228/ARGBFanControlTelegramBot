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

colorWipeRouter = Router()

@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_1), F.text.in_(names["colors"]["basicColors"].values()))
async def colorPick(message: Message, state: FSMContext):
    colorIndex = int(list(names["colors"]["basicColors"].values()).index(message.text))
    color = list(names["colors"]["basicColors"].keys())[colorIndex]
    logger.info(f"Выбран {color.capitalize()} для Color Wipe")
    await state.update_data(COLOR_1=f"{color.upper()}")
    await state.set_state(StateMachine.COLOR_WIPE_2)
    await message.answer(names["colors"]["basicColors"][f"{color}"] + ' установлен в качестве первого цвета для ' + (names["custom"]["colorwipe"]) + '\nВыбери второй')

@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_2), F.text.in_(names["colors"]["basicColors"].values()))
async def colorPick(message: Message, state: FSMContext):
    colorIndex = int(list(names["colors"]["basicColors"].values()).index(message.text))
    color = list(names["colors"]["basicColors"].keys())[colorIndex]
    logger.info("Выбран Red для Color Wipe 2")
    await message.answer(names["colors"]["basicColors"][f"{color}"] + ' установлен в качестве второго цвета для ' + (names["custom"]["colorwipe"]))
    color1 = await state.get_data()
    await state.set_state(StateMachine.CUSTOM_PRESETS)
    FanController.colorwipe(color1["COLOR_1"], f'{color.upper()}')






"""
    "fire": "\uD83D\uDD25 огонь",
    "ocean": "\uD83C\uDF0A океан"
"""