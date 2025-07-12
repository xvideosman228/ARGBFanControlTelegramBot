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

cylonRouter = Router()

@exception
@cylonRouter.message(StateFilter(StateMachine.CYLON), F.text.in_(names["times"].values()))
async def timePick(message: Message, state: FSMContext):
    timeIndex = int(list(names["times"].values()).index(message.text))
    time = list(names["times"].keys())[timeIndex]
    logger.info(f"Выбран {time} для Cylon")

    await message.answer(names["times"][f"{time}"] + ' установлено в качестве времени для ' + (names["custom"]["cylon"]),reply_markup=customPresetsKeyboard)
    await state.set_state(StateMachine.CUSTOM_PRESETS)
    FanController.cylon(time)
