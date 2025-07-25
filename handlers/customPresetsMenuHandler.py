from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import or_f
from handlers.colorWipeHandler import colorWipeRouter
from handlers.cylonHandler import cylonRouter
from handlers.fadeInOutHandler import fadeInOutRouter
from handlers.gradient4Handler import gradient4Router
from handlers.gradientHandler import gradientRouter
from handlers.smoothGradientHandler import smoothGradientRouter
from keyboard import customPresetsKeyboard, colorKeyboard, timeKeyboard, preinstalledGradient4Keyboard, \
    generatePreinstalledGradient4Keyboard, longTimesKeyboard
from serialControl import FanController
from stateMachine import StateMachine
from config.loggingConfig import exception, logger
import json

with open('./config/buttons.json') as file:
    names = json.load(file)

with open('./config/texts.json') as file:
    texts = json.load(file)

customPresetsMenuRouter = Router()
customPresetsMenuRouter.include_routers(fadeInOutRouter, colorWipeRouter, gradientRouter, smoothGradientRouter, gradient4Router, cylonRouter)


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

'''
@exception
@customPresetsMenuRouter.message(StateFilter(StateMachine.CUSTOM_PRESETS), F.text == names["custom"]["runninglights"])
async def runninglight(message: Message):
    logger.info("Кнопка Runnung Lights нажата")
    await message.answer(texts["runninglights"])
    FanController.runninglight()
    
"runninglights": "Running Lights",    

'''

@exception
@customPresetsMenuRouter.message(StateFilter(StateMachine.CUSTOM_PRESETS), F.text == names["custom"]["gradient"])
async def gradient(message: Message, state: FSMContext):
    logger.info("Кнопка Gradient нажата")
    await state.set_state(StateMachine.GRADIENT_1)
    await message.answer(texts["gradient"], reply_markup=colorKeyboard)

@exception
@customPresetsMenuRouter.message(StateFilter(StateMachine.CUSTOM_PRESETS), F.text == names["custom"]["gradient4"])
async def gradient4(message: Message, state: FSMContext):
    logger.info("Кнопка Gradient4 нажата")
    preinstalledGradient4Keyboard = generatePreinstalledGradient4Keyboard()
    await state.set_state(StateMachine.GRADIENT4)
    await message.answer(texts["gradient4"], reply_markup=preinstalledGradient4Keyboard)

@exception
@customPresetsMenuRouter.message(StateFilter(StateMachine.CUSTOM_PRESETS), F.text == names["custom"]["smoothGradient"])
async def smoothGradient(message: Message, state: FSMContext):
    logger.info("Кнопка Smooth Gradient нажата")
    await state.set_state(StateMachine.SMOOTH_GRADIENT_1)
    await message.answer(texts["smoothGradient"], reply_markup=colorKeyboard)

@exception
@customPresetsMenuRouter.message(StateFilter(StateMachine.CUSTOM_PRESETS), F.text == names["custom"]["cylon"])
async def cylon(message: Message, state: FSMContext):
    logger.info("Кнопка Cylon нажата")
    await state.set_state(StateMachine.CYLON)
    await message.answer(texts["cylon"], reply_markup=longTimesKeyboard)

@exception
@customPresetsMenuRouter.message(StateFilter(StateMachine.CUSTOM_PRESETS), F.text == names["custom"]["pacific"])
async def pacific(message: Message):
    logger.info("Кнопка Pacific нажата")
    await message.answer(texts["pacific"])
    FanController.pacific()

@exception
@customPresetsMenuRouter.message(StateFilter(StateMachine.CUSTOM_PRESETS), F.text)
async def default(message: Message, state: FSMContext):
    logger.info(f"Пользователь {message.from_user.id} написал неразборчивый текст")
    await message.answer(texts['iDidNotFuckingUnderstandYouStupidMoron'], reply_markup=customPresetsKeyboard)


states = (
    StateMachine.FADE_IN_OUT,
    StateMachine.GRADIENT_1,
    StateMachine.GRADIENT_2,
    StateMachine.SMOOTH_GRADIENT_1,
    StateMachine.SMOOTH_GRADIENT_2,
    StateMachine.COLOR_WIPE_1,
    StateMachine.COLOR_WIPE_2,
    StateMachine.COLOR_WIPE_TIME,
    StateMachine.GRADIENT4_1,
    StateMachine.GRADIENT4,
    StateMachine.GRADIENT4_2,
    StateMachine.GRADIENT4_3,
    StateMachine.GRADIENT4_4,
    StateMachine.CYLON
)
@exception
@customPresetsMenuRouter.message(or_f(StateFilter(*states)), F.text == names["back"])
async def back(message: Message, state: FSMContext):
    await state.set_state(StateMachine.CUSTOM_PRESETS)
    await message.answer(texts['custom'], reply_markup=customPresetsKeyboard)

"""
    "fire": "\uD83D\uDD25 огонь",
    "ocean": "\uD83C\uDF0A океан"
"""