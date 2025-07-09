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

gradientRouter = Router()

@exception
@gradientRouter.message(StateFilter(StateMachine.GRADIENT_1), F.text.in_(names["colors"]["basicColors"].values()))
async def colorPick(message: Message, state: FSMContext):
    colorIndex = int(list(names["colors"]["basicColors"].values()).index(message.text))
    color = list(names["colors"]["basicColors"].keys())[colorIndex]
    logger.info(f"Выбран {color.capitalize()} для Gradient")

    await state.update_data(GRADIENT_COLOR_1=f"{color.upper()}")
    await state.set_state(StateMachine.GRADIENT_2)
    await message.answer(names["colors"]["basicColors"][f"{color}"] + ' установлен в качестве первого цвета для ' + names["custom"]["gradient"] + '\nВыбери второй', reply_markup=colorKeyboard)

@exception
@gradientRouter.message(StateFilter(StateMachine.GRADIENT_2), F.text.in_(names["colors"]["basicColors"].values()))
async def colorPick(message: Message, state: FSMContext):
    colorIndex = int(list(names["colors"]["basicColors"].values()).index(message.text))
    color = list(names["colors"]["basicColors"].keys())[colorIndex]
    logger.info(f"Выбран {color.capitalize()} для Gradient")

    await state.update_data(GRADIENT_COLOR_2=f"{color.upper()}")
    await state.set_state(StateMachine.CUSTOM_PRESETS)
    await message.answer(names["colors"]["basicColors"][f"{color}"] + ' установлен в качестве второго цвета для ' + names["custom"]["gradient"], reply_markup=customPresetsKeyboard)
    color = await state.get_data()
    FanController.gradient(f'{color["GRADIENT_COLOR_1"]}', f'{color["GRADIENT_COLOR_2"]}')
