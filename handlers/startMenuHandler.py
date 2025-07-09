from aiogram.filters import StateFilter, or_f
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram import Router, F
from aiogram.types import Message
from keyboard import startKeyboard, backKeyboard, customPresetsKeyboard
from stateMachine import StateMachine
from config.loggingConfig import exception, logger
from serialControl import FanController
from handlers.customPresetsMenuHandler import customPresetsMenuRouter
import json


with open('./config/buttons.json') as file:
    names = json.load(file)

with open('./config/texts.json') as file:
    texts = json.load(file)


startMenuRouter = Router()
startMenuRouter.include_router(customPresetsMenuRouter)

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
@startMenuRouter.message(StateFilter(StateMachine.START), F.text == names["startButtons"]["mode+"])
async def modeplus(message: Message):
    logger.info("Кнопка Mode + нажата")
    await message.answer(texts["mode+"])

@exception
@startMenuRouter.message(StateFilter(StateMachine.START), F.text == names["startButtons"]["mode-"])
async def modeminus(message: Message):
    logger.info("Кнопка Mode - нажата")
    await message.answer(texts["mode-"])




async def color(message):
    colourIndex = int(list(names["colors"]["basicColors"].values()).index(message.text))
    logger.info(f"Кнопка {message.text.capitalize()} нажата")
    colour = list(names["colors"]["basicColors"].keys())[colourIndex]
    print(colour)
    await message.answer(texts[colour])
    FanController.color(colour.upper())




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
    FanController.brightnessplusplus()
    await message.answer(texts["brightness++"])

@exception
@startMenuRouter.message(StateFilter(StateMachine.START), F.text == names["startButtons"]["brightness--"])
async def brightnessminusminus(message: Message):
    logger.info("Кнопка Brightness -- нажата")
    FanController.brightnessminusminus()
    await message.answer(texts["brightness--"])

@exception
@startMenuRouter.message(StateFilter(StateMachine.START), F.text == names["colors"]["basicColors"]["black"])
async def black(message: Message):
    logger.info("Кнопка Black нажата")
    await message.answer(texts["black"])
    FanController.black()

@exception
@startMenuRouter.message(StateFilter(StateMachine.START), F.text == names["customPresets"])
async def custom(message: Message, state: FSMContext):
    await state.set_state(StateMachine.CUSTOM_PRESETS)
    logger.info("Кнопка с кастомными пресетами нажата")
    await message.answer(texts["custom"], reply_markup=customPresetsKeyboard)


@exception
@startMenuRouter.message(StateFilter(StateMachine.CUSTOM_PRESETS),F.text == names["back"])
async def back(message: Message, state: FSMContext):
    await state.set_state(StateMachine.START)
    await message.answer(texts['start'], reply_markup=startKeyboard)

@exception
@startMenuRouter.message(StateFilter(StateMachine.START), F.text)
async def default(message: Message, state: FSMContext):
    if message.text in list(names["colors"]["basicColors"].values()):
        await color(message)
    # logger.info(f"Пользователь {message.from_user.id} чёто сказал")
    await state.set_state(StateMachine.START)
    await message.answer(texts['iDidNotFuckingUnderstandYouStupidMoron'], reply_markup=startKeyboard)

"""
Генератор кода для цветов
@exception
@startMenuRouter.message(StateFilter(StateMachine.START), F.text == names["colors"]["basicColors"]["red"])
async def red(message: Message):
    logger.info("Кнопка red нажата")
    await message.answer(texts["red"])
    for x in names["colors"]["basicColors"].keys():
        print(f"
@exception
@startMenuRouter.message(StateFilter(StateMachine.START), F.text == names["colors"]["basicColors"]["{x}"])
async def {x}(message: Message):
    logger.info("Кнопка {x.capitalize()} нажата")
    await message.answer(texts["{x}"])")

"""
