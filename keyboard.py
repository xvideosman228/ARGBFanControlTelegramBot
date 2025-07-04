from aiogram.types import ReplyKeyboardMarkup, KeyboardButton as Key, InlineKeyboardButton as Ikey, \
    InlineKeyboardMarkup
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


backKeyboard = ReplyKeyboard(keyboard=[
        [Back()]])

