from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.types import Message

from keyboard import customPresetsKeyboard
from serialControl import FanController
from stateMachine import StateMachine
from config.loggingConfig import exception, logger
import json

with open('./config/buttons.json') as file:
    names = json.load(file)

with open('./config/texts.json') as file:
    texts = json.load(file)

customPresetsMenuRouter = Router()


@exception
@customPresetsMenuRouter.message(StateFilter(StateMachine.CUSTOM_PRESETS), F.text == names["customPresets"])
async def fanConfig(message: Message):
    logger.info("Кнопка Fan Config нажата")
    await message.answer(texts["fanConfig"])

@exception
@customPresetsMenuRouter.message(StateFilter(StateMachine.CUSTOM_PRESETS), F.text == names["custom"]["colorwipe"])
async def colorwipe(message: Message):
    logger.info("Кнопка Color Wipe нажата")
    await message.answer(texts["colorWipe"])
    FanController.colorWipe()

@exception
@customPresetsMenuRouter.message(StateFilter(StateMachine.CUSTOM_PRESETS), F.text == names["custom"]["fadeinout"])
async def fadeinout(message: Message):
    logger.info("Кнопка Fade in/out нажата")
    await message.answer(texts["fadeinout"])
    FanController.fadeinout()

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


"""
    "fire": "\uD83D\uDD25 огонь",
    "ocean": "\uD83C\uDF0A океан"
"""