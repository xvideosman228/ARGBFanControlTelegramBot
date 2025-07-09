from aiogram.types import ReplyKeyboardMarkup, KeyboardButton as Key, InlineKeyboardButton as Ikey, \
    InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from functools import partial
import json

with open("config/buttons.json") as file:
    names = json.load(file)

with open("config/presets.json") as file:
    presets = json.load(file)

ReplyKeyboard = partial(ReplyKeyboardMarkup, resize_keyboard=True)
InlineKeyboard = partial(InlineKeyboardMarkup)
Back = partial(Key, text='⬅️ Назад')


def generateStartKeyboard():
    builder = ReplyKeyboardBuilder()
    buttons = [x for x in names["startButtons"].values()]
    for button in buttons:
        builder.button(text=button)
    builder.button(text=names['customPresets'])
    for text in names["colors"]['basicColors'].values():
        builder.button(text=f"{text}")
    builder.adjust(5,5,1,7,6)

    return builder.as_markup()


def generateCustomPresetsKeyboard():
    builder = ReplyKeyboardBuilder()
    buttons = [x for x in names["custom"].values()]
    for button in buttons:
        builder.button(text=button)
    builder.button(text='⬅️ Назад')
    builder.adjust(3,3,2,1)

    return builder.as_markup()

def generatePreinstalledGradient4Keyboard():
    builder = ReplyKeyboardBuilder()
    buttons = [x for x in presets["gradient4"].keys()]
    for button in buttons:
        builder.button(text=button)
    builder.button(text=names["make"])
    builder.button(text='⬅️ Назад')
    builder.adjust( 3,3, 1, 1)

    return builder.as_markup()

def generateColorKeyboard():
    builder = ReplyKeyboardBuilder()
    buttons = [x for x in names["colors"]["basicColors"].values()]
    for button in buttons:
        builder.button(text=button)
    builder.button(text='⬅️ Назад')
    builder.adjust(7,6, 1)

    return builder.as_markup()

def generateTimeKeyboard():
    builder = ReplyKeyboardBuilder()
    buttons = [x for x in names["times"].values()]
    for button in buttons:
        builder.button(text=button)
    builder.button(text='⬅️ Назад')
    builder.adjust(5,5, 1)

    return builder.as_markup()

def generateShortTimeKeyboard():
    builder = ReplyKeyboardBuilder()
    buttons = [x for x in names["shortTimes"].values()]
    for button in buttons:
        builder.button(text=button)
    builder.button(text='⬅️ Назад')
    builder.adjust(3,3,3, 1)

    return builder.as_markup()

colorKeyboard = generateColorKeyboard()
startKeyboard = generateStartKeyboard()
customPresetsKeyboard = generateCustomPresetsKeyboard()
timeKeyboard = generateTimeKeyboard()
shortTimeKeyboard = generateShortTimeKeyboard()
preinstalledGradient4Keyboard = generatePreinstalledGradient4Keyboard()

backKeyboard = ReplyKeyboard(keyboard=[[Back()]])


