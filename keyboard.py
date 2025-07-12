from aiogram.types import ReplyKeyboardMarkup, KeyboardButton as Key, InlineKeyboardButton as Ikey, \
    InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from functools import partial
import json

with open("config/buttons.json") as file:
    names = json.load(file)

def jsonUpdate():
    with open('./config/presets.json') as file:
        presets = json.load(file)
    return presets
ReplyKeyboard = partial(ReplyKeyboardMarkup, resize_keyboard=True)
InlineKeyboard = partial(InlineKeyboardMarkup)
Back = partial(Key, text='⬅️ Назад')


def generateStartKeyboard():
    builder = ReplyKeyboardBuilder()
    buttons = [x for x in names["startButtons"].values()]
    for button in buttons:
        builder.button(text=button)
    for text in names["colors"]['basicColors'].values():
        builder.button(text=f"{text}")


    builder.adjust(5,9,8)

    return builder.as_markup()


def generateCustomPresetsKeyboard():
    builder = ReplyKeyboardBuilder()
    rowNumber = 4
    buttons = [x for x in names["custom"].values()]
    firstRow = len(buttons) // 2
    sizesTuple = ((rowNumber,) * (len(buttons) // rowNumber)) + (len(buttons) % rowNumber,)
    sizesTuple = tuple(x for x in sizesTuple if x != 0)
    for button in buttons:
        builder.button(text=button)
    builder.button(text='⬅️ Назад')
    builder.adjust(*sizesTuple,1)

    return builder.as_markup()

def generatePreinstalledGradient4Keyboard():
    builder = ReplyKeyboardBuilder()
    rowNumber = 3
    buttons = [x for x in jsonUpdate().keys()]
    firstRow = len(buttons) // 2
    sizesTuple = ((rowNumber,) * (len(buttons) // rowNumber)) + (len(buttons) % rowNumber,)
    sizesTuple = tuple(x for x in sizesTuple if x != 0)
    builder.button(text=names["random4gradient"])
    builder.button(text=names["make"])
    for button in buttons:
        builder.button(text=button)
    builder.button(text='⬅️ Назад')
    builder.adjust(2, *sizesTuple, 1)

    return builder.as_markup()

def generateColorKeyboard():
    builder = ReplyKeyboardBuilder()
    rowNumber = 8
    buttons = [x for x in names["colors"]["basicColors"].values()]
    firstRow = len(buttons) // 2
    sizesTuple = ((rowNumber,) * (len(buttons) // rowNumber)) + (len(buttons) % rowNumber,)
    sizesTuple = tuple(x for x in sizesTuple if x != 0)
    for button in buttons:
        builder.button(text=button)
    builder.button(text='⬅️ Назад')
    builder.adjust(*sizesTuple, 1)

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

def generateLongTimeKeyboard():
    builder = ReplyKeyboardBuilder()
    buttons = [x for x in names["longTimes"].values()]
    for button in buttons:
        builder.button(text=button)
    builder.button(text='⬅️ Назад')
    builder.adjust(3,2, 1)

    return builder.as_markup()

colorKeyboard = generateColorKeyboard()
startKeyboard = generateStartKeyboard()
customPresetsKeyboard = generateCustomPresetsKeyboard()
timeKeyboard = generateTimeKeyboard()
shortTimeKeyboard = generateShortTimeKeyboard()
preinstalledGradient4Keyboard = generatePreinstalledGradient4Keyboard()
addToFavoritesKeyboard = InlineKeyboard(inline_keyboard=[[Ikey(text=names["addToFavorites"], callback_data='favorite')]])
longTimesKeyboard = generateLongTimeKeyboard()
backKeyboard = ReplyKeyboard(keyboard=[[Back()]])


"""
    "strength-": "♨\uD83D\uDD3D",
    "strength--": "♨⏬",
    "mode-": "⚙\uFE0F\uD83D\uDD3D",
        "strength+": "♨\uD83D\uDD3C",
    "strength++": "♨⏫",
    "mode+": "⚙\uFE0F\uD83D\uDD3C",
"""