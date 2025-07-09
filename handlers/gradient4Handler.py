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

with open('./config/presets.json') as file:
    presets = json.load(file)

gradient4Router = Router()

@exception
@gradient4Router.message(StateFilter(StateMachine.GRADIENT4), F.text.in_(presets["gradient4"].keys()))
async def color(message: Message, state: FSMContext):
    print(message.text)
    colors = presets["gradient4"].get(message.text)
    colors = colors.split()
    print(colors)
    color1, color2, color3, color4 = colors[0], colors[1], colors[2], colors[3]
    await message.answer(f"{message.text}-градиент", reply_markup=customPresetsKeyboard)
    FanController.gradient4(color1, color2, color3, color4)
    await state.set_state(StateMachine.CUSTOM_PRESETS)

@exception
@gradient4Router.message(StateFilter(StateMachine.GRADIENT4), F.text == names["make"])
async def make(message: Message, state: FSMContext):
    await state.set_state(StateMachine.GRADIENT4_1)
    await message.answer('Выбери 1-й цвет', reply_markup=colorKeyboard)

@exception
@gradient4Router.message(StateFilter(StateMachine.GRADIENT4_1), F.text.in_(names["colors"]["basicColors"].values()))
async def colorPick(message: Message, state: FSMContext):
    colorIndex = int(list(names["colors"]["basicColors"].values()).index(message.text))
    color = list(names["colors"]["basicColors"].keys())[colorIndex]
    logger.info(f"Выбран {color.capitalize()} для 4Gradient_1")

    await state.update_data(GRADIENT4_COLOR_1=f"{color.upper()}")
    await state.set_state(StateMachine.GRADIENT4_2)
    await message.answer(names["colors"]["basicColors"][f"{color}"] + ' установлен в качестве первого цвета для ' + names["custom"]["gradient4"] + '\nВыбери второй', reply_markup=colorKeyboard)

@exception
@gradient4Router.message(StateFilter(StateMachine.GRADIENT4_2), F.text.in_(names["colors"]["basicColors"].values()))
async def colorPick(message: Message, state: FSMContext):
    colorIndex = int(list(names["colors"]["basicColors"].values()).index(message.text))
    color = list(names["colors"]["basicColors"].keys())[colorIndex]
    logger.info(f"Выбран {color.capitalize()} для 4Gradient_2")

    await state.update_data(GRADIENT4_COLOR_2=f"{color.upper()}")
    await state.set_state(StateMachine.GRADIENT4_3)
    await message.answer(names["colors"]["basicColors"][f"{color}"] + ' установлен в качестве второго цвета для ' + names["custom"]["gradient4"] + '\nВыбери третий', reply_markup=colorKeyboard)

@exception
@gradient4Router.message(StateFilter(StateMachine.GRADIENT4_3), F.text.in_(names["colors"]["basicColors"].values()))
async def colorPick(message: Message, state: FSMContext):
    colorIndex = int(list(names["colors"]["basicColors"].values()).index(message.text))
    color = list(names["colors"]["basicColors"].keys())[colorIndex]
    logger.info(f"Выбран {color.capitalize()} для 4Gradient_3")

    await state.update_data(GRADIENT4_COLOR_3=f"{color.upper()}")
    await state.set_state(StateMachine.GRADIENT4_4)
    await message.answer(names["colors"]["basicColors"][f"{color}"] + ' установлен в качестве третьего цвета для ' + names["custom"]["gradient4"] + '\nВыбери четвёртый', reply_markup=colorKeyboard)



@exception
@gradient4Router.message(StateFilter(StateMachine.GRADIENT4_4), F.text.in_(names["colors"]["basicColors"].values()))
async def colorPick(message: Message, state: FSMContext):
    colorIndex = int(list(names["colors"]["basicColors"].values()).index(message.text))
    color = list(names["colors"]["basicColors"].keys())[colorIndex]
    logger.info(f"Выбран {color.capitalize()} для 4Gradient_4")

    await state.update_data(GRADIENT4_COLOR_4=f"{color.upper()}")
    await message.answer(names["colors"]["basicColors"][f"{color}"] + ' установлен в качестве четвёртого цвета для ' + names["custom"]["gradient4"], reply_markup=customPresetsKeyboard)
    color = await state.get_data()
    FanController.gradient4(f'{color["GRADIENT4_COLOR_1"]}', f'{color["GRADIENT4_COLOR_2"]}', f'{color["GRADIENT4_COLOR_3"]}', f'{color["GRADIENT4_COLOR_4"]}')
    await state.set_state(StateMachine.CUSTOM_PRESETS)