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
@fadeInOutRouter.message(StateFilter(StateMachine.FADE_IN_OUT), F.text == names["colors"]["basicColors"]["red"])
async def red(message: Message):
    logger.info("Выбран Red для Fade In / Out")
    await message.answer(names["colors"]["basicColors"]["red"] + ' для ' + names["custom"]["fadeinout"])
    FanController.fadeinout('RED')

@exception
@fadeInOutRouter.message(StateFilter(StateMachine.FADE_IN_OUT), F.text == names["colors"]["basicColors"]["green"])
async def green(message: Message):
    logger.info("Выбран Green для Fade In / Out")
    await message.answer(names["colors"]["basicColors"]["green"] + ' для ' + names["custom"]["fadeinout"])
    FanController.fadeinout('GREEN')

@exception
@fadeInOutRouter.message(StateFilter(StateMachine.FADE_IN_OUT), F.text == names["colors"]["basicColors"]["blue"])
async def blue(message: Message):
    logger.info("Выбран Blue для Fade In / Out")
    await message.answer(names["colors"]["basicColors"]["blue"] + ' для ' + names["custom"]["fadeinout"])
    FanController.fadeinout('BLUE')

@exception
@fadeInOutRouter.message(StateFilter(StateMachine.FADE_IN_OUT), F.text == names["colors"]["basicColors"]["yellow"])
async def yellow(message: Message):
    logger.info("Выбран Yellow для Fade In / Out")
    await message.answer(names["colors"]["basicColors"]["yellow"] + ' для ' + names["custom"]["fadeinout"])
    FanController.fadeinout('YELLOW')

@exception
@fadeInOutRouter.message(StateFilter(StateMachine.FADE_IN_OUT), F.text == names["colors"]["basicColors"]["yelloworange"])
async def yelloworange(message: Message):
    logger.info("Выбран Yelloworange для Fade In / Out")
    await message.answer(names["colors"]["basicColors"]["yelloworange"] + ' для ' + names["custom"]["fadeinout"])
    FanController.fadeinout('YELLOWORANGE')

@exception
@fadeInOutRouter.message(StateFilter(StateMachine.FADE_IN_OUT), F.text == names["colors"]["basicColors"]["orange"])
async def orange(message: Message):
    logger.info("Выбран Orange для Fade In / Out")
    await message.answer(names["colors"]["basicColors"]["orange"] + ' для ' + names["custom"]["fadeinout"])
    FanController.fadeinout('ORANGE')

@exception
@fadeInOutRouter.message(StateFilter(StateMachine.FADE_IN_OUT), F.text == names["colors"]["basicColors"]["orangered"])
async def orangered(message: Message):
    logger.info("Выбран Orangered для Fade In / Out")
    await message.answer(names["colors"]["basicColors"]["orangered"] + ' для ' + names["custom"]["fadeinout"])
    FanController.fadeinout('ORANGERED')

@exception
@fadeInOutRouter.message(StateFilter(StateMachine.FADE_IN_OUT), F.text == names["colors"]["basicColors"]["lightblue"])
async def lightblue(message: Message):
    logger.info("Выбран Lightblue для Fade In / Out")
    await message.answer(names["colors"]["basicColors"]["lightblue"] + ' для ' + names["custom"]["fadeinout"])
    FanController.fadeinout('LIGHTBLUE')

@exception
@fadeInOutRouter.message(StateFilter(StateMachine.FADE_IN_OUT), F.text == names["colors"]["basicColors"]["darkblue"])
async def darkblue(message: Message):
    logger.info("Выбран Darkblue для Fade In / Out")
    await message.answer(names["colors"]["basicColors"]["darkblue"] + ' для ' + names["custom"]["fadeinout"])
    FanController.fadeinout('DARKBLUE')

@exception
@fadeInOutRouter.message(StateFilter(StateMachine.FADE_IN_OUT), F.text == names["colors"]["basicColors"]["violet"])
async def violet(message: Message):
    logger.info("Выбран Violet для Fade In / Out")
    await message.answer(names["colors"]["basicColors"]["violet"] + ' для ' + names["custom"]["fadeinout"])
    FanController.fadeinout('VIOLET')

@exception
@fadeInOutRouter.message(StateFilter(StateMachine.FADE_IN_OUT), F.text == names["colors"]["basicColors"]["white"])
async def white(message: Message):
    logger.info("Выбран White для Fade In / Out")
    await message.answer(names["colors"]["basicColors"]["white"] + ' для ' + names["custom"]["fadeinout"])
    FanController.fadeinout('WHITE')







@exception
@fadeInOutRouter.message(StateFilter(StateMachine.FADE_IN_OUT))
async def colorChoose(message: Message, state: FSMContext):
    logger.info("Открыто меню выбора цвета для Fade in / out")
    await message.answer(texts["chooseColor"], reply_markup=colorKeyboard)


"""
    "fire": "\uD83D\uDD25 огонь",
    "ocean": "\uD83C\uDF0A океан"
"""