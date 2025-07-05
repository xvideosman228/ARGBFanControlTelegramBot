from aiogram.types import ReplyKeyboardMarkup, KeyboardButton as Key, InlineKeyboardButton as Ikey, \
    InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from functools import partial
import json

with open("config/buttons.json") as file:
    names = json.load(file)

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
    builder.adjust(5,5,1,5,5)

    return builder.as_markup()


def generateCustomPresetsKeyboard():
    builder = ReplyKeyboardBuilder()
    buttons = [x for x in names["custom"].values()]
    for button in buttons:
        builder.button(text=button)
    builder.button(text='⬅️ Назад')
    builder.adjust(3,3,3,1)

    return builder.as_markup()

startKeyboard = generateStartKeyboard()
customPresetsKeyboard = generateCustomPresetsKeyboard()


backKeyboard = ReplyKeyboard(keyboard=[[Back()]])


