from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.types import Message

from keyboard import shortTimeKeyboard, customPresetsKeyboard
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
    await state.update_data(COLOR_1_COLOR_WIPE=f"{color.upper()}")
    await state.set_state(StateMachine.COLOR_WIPE_2)
    await message.answer(names["colors"]["basicColors"][f"{color}"] + ' установлен в качестве первого цвета для ' + (names["custom"]["colorwipe"]) + '\nВыбери второй')

@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_2), F.text.in_(names["colors"]["basicColors"].values()))
async def colorPick(message: Message, state: FSMContext):
    colorIndex = int(list(names["colors"]["basicColors"].values()).index(message.text))
    color = list(names["colors"]["basicColors"].keys())[colorIndex]
    logger.info(f"Выбран {color.capitalize()} для Color Wipe 2")
    await state.update_data(COLOR_2_COLOR_WIPE=f"{color.upper()}")
    await message.answer(names["colors"]["basicColors"][f"{color}"] + ' установлен в качестве второго цвета для ' + (names["custom"]["colorwipe"]), reply_markup=shortTimeKeyboard)
    await state.set_state(StateMachine.COLOR_WIPE_TIME)

@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_TIME), F.text.in_(names["shortTimes"].values()))
async def timePick(message: Message, state: FSMContext):
    timeIndex = int(list(names["shortTimes"].values()).index(message.text))
    time = list(names["shortTimes"].keys())[timeIndex]
    logger.info(f"Выбран {time} для Color Wipe 2")

    await message.answer(names["shortTimes"][f"{time}"] + ' установлено в качестве времени для ' + (names["custom"]["colorwipe"]), reply_markup=customPresetsKeyboard)
    color = await state.get_data()
    await state.set_state(StateMachine.CUSTOM_PRESETS)
    FanController.colorwipe(f'{color["COLOR_1_COLOR_WIPE"]}', f'{color["COLOR_2_COLOR_WIPE"]}' ,  f'{time.upper()}')






"""
    "fire": "\uD83D\uDD25 огонь",
    "ocean": "\uD83C\uDF0A океан"
"""