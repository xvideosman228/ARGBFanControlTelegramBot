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


startKeyboard = ReplyKeyboard(keyboard=[
        [Key(text=names['fanConfig'])], [Key(text=names['about'])]])

fanConfigKeyboard = ReplyKeyboard(keyboard=[
        [Key(text=names['fans']['preinstalled'])], [Key(text=names['fans']['colors'])], [Back()]])

def generatePreinstalledFanConfigKeyboard():
    builder = ReplyKeyboardBuilder()
    for text in names['preinstalled'].values():
        builder.button(text=f"{text}")
    builder.add(Back())
    builder.adjust(3,3,3, 1)

    return builder.as_markup()

preinstalledFanConfigKeyboard = generatePreinstalledFanConfigKeyboard()

def generateColorsFanConfigKeyboard():
    builder = ReplyKeyboardBuilder()
    for text in names['colors']['basicColors'].values():
        builder.button(text=f"{text}")
    builder.add(Back())
    builder.adjust(3, 1)

    return builder.as_markup()

colorsFanConfigKeyboard = generateColorsFanConfigKeyboard()

backKeyboard = ReplyKeyboard(keyboard=[
        [Back()]])

