from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import or_f
from handlers.colorWipeHandler import colorWipeRouter
from handlers.fadeInOutHandler import fadeInOutRouter
from handlers.gradientHandler import gradientRouter
from keyboard import customPresetsKeyboard, colorKeyboard
from serialControl import FanController
from stateMachine import StateMachine
from config.loggingConfig import exception, logger
import json

with open('./config/buttons.json') as file:
    names = json.load(file)

with open('./config/texts.json') as file:
    texts = json.load(file)

customPresetsMenuRouter = Router()
customPresetsMenuRouter.include_routers(fadeInOutRouter, colorWipeRouter, gradientRouter)


@exception
@customPresetsMenuRouter.message(StateFilter(StateMachine.CUSTOM_PRESETS), F.text == names["customPresets"])
async def fanConfig(message: Message):
    logger.info("Кнопка Fan Config нажата")
    await message.answer(texts["fanConfig"])

@exception
@customPresetsMenuRouter.message(StateFilter(StateMachine.CUSTOM_PRESETS), F.text == names["custom"]["colorwipe"])
async def colorwipe(message: Message, state: FSMContext):
    logger.info("Кнопка Color Wipe нажата")
    await state.set_state(StateMachine.COLOR_WIPE_1)
    await message.answer(texts["colorWipe1"], reply_markup=colorKeyboard)

@exception
@customPresetsMenuRouter.message(StateFilter(StateMachine.CUSTOM_PRESETS), F.text == names["custom"]["fadeinout"])
async def fadeinout(message: Message, state: FSMContext):
    logger.info("Кнопка Fade in/out нажата")
    await state.set_state(StateMachine.FADE_IN_OUT)
    await message.answer(texts["fadeinout"], reply_markup=colorKeyboard)

@exception
@customPresetsMenuRouter.message(StateFilter(StateMachine.CUSTOM_PRESETS), F.text == names["custom"]["rainbow"])
async def rainbow(message: Message):
    logger.info("Кнопка Rainbow нажата")
    await message.answer(texts["rainbow"])
    FanController.rainbow()

@exception
@customPresetsMenuRouter.message(StateFilter(StateMachine.CUSTOM_PRESETS), F.text == names["custom"]["runninglights"])
async def runninglight(message: Message):
    logger.info("Кнопка Runnung Lights нажата")
    await message.answer(texts["runninglights"])
    FanController.runninglight()

@exception
@customPresetsMenuRouter.message(StateFilter(StateMachine.CUSTOM_PRESETS), F.text == names["custom"]["gradient"])
async def gradient(message: Message, state: FSMContext):
    logger.info("Кнопка Gradient нажата")
    await state.set_state(StateMachine.GRADIENT_1)
    await message.answer(texts["gradient"], reply_markup=colorKeyboard)

@exception
@customPresetsMenuRouter.message(StateFilter(StateMachine.CUSTOM_PRESETS), F.text == names["custom"]["cylon"])
async def cylon(message: Message):
    logger.info("Кнопка Cylon нажата")
    await message.answer(texts["cylon"])
    FanController.cylon()

@exception
@customPresetsMenuRouter.message(StateFilter(StateMachine.CUSTOM_PRESETS), F.text == names["custom"]["pacific"])
async def pacific(message: Message):
    logger.info("Кнопка Pacific нажата")
    await message.answer(texts["pacific"])
    FanController.pacific()

@exception
@customPresetsMenuRouter.message(StateFilter(StateMachine.CUSTOM_PRESETS), F.text)
async def default(message: Message, state: FSMContext):
    logger.info(f"Пользователь {message.from_user.id} чёто непонятное сказал")
    await message.answer(texts['iDidNotFuckingUnderstandYouStupidMoron'], reply_markup=customPresetsKeyboard)

@exception
@customPresetsMenuRouter.message(or_f(StateFilter(StateMachine.FADE_IN_OUT), StateFilter(StateMachine.COLOR_WIPE_1)),F.text == names["back"])
async def back(message: Message, state: FSMContext):
    await state.set_state(StateMachine.CUSTOM_PRESETS)
    await message.answer(texts['start'], reply_markup=customPresetsKeyboard)

"""
    "fire": "\uD83D\uDD25 огонь",
    "ocean": "\uD83C\uDF0A океан"
"""