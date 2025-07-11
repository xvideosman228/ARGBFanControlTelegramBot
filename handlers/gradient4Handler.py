from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from random import choice
from keyboard import customPresetsKeyboard, colorKeyboard, addToFavoritesKeyboard
from serialControl import FanController
from stateMachine import StateMachine
from config.loggingConfig import exception, logger
import json

with open('./config/buttons.json') as file:
    names = json.load(file)

with open('./config/texts.json') as file:
    texts = json.load(file)


gradient4Router = Router()

# 🎲
# Функция для получения всех предустановленных наборов градиентов
def jsonUpdate():
    with open('./config/presets.json', encoding='utf-8') as file:
        presets = json.load(file)
        return presets


# Фильтр состояния и проверка текста сообщения
@gradient4Router.message(StateFilter(StateMachine.GRADIENT4), F.text.in_(jsonUpdate().keys()))
async def color(message: Message):
    presets = jsonUpdate()
    # Прямо получаем нужное значение по переданному сообщению
    colors_str = presets.get(message.text)
    if not colors_str:
        await message.answer("Такой градиент не найден.", reply_markup=customPresetsKeyboard)
        return

    # Разделяем строку цветов пробелами
    colors = colors_str.strip().split()
    color1, color2, color3, color4 = colors[:4]

    # Отправляем сообщение и запускаем команду контроллера вентилятора
    await message.answer(f"{message.text}-градиент")
    FanController.gradient4(color1, color2, color3, color4)

@exception
@gradient4Router.message(StateFilter(StateMachine.GRADIENT4), F.text == names["random4gradient"])
async def randomColor(message: Message, state: FSMContext):
    colors = [choice(list(names["colors"]["basicColors"].keys())).upper() for x in range(4)]
    color1, color2, color3, color4 = colors[0], colors[1], colors[2], colors[3]
    emojis = [names["colors"]["basicColors"][x.lower()] for x in colors]
    await message.answer(f"{"".join(emojis)}-градиент", reply_markup=addToFavoritesKeyboard)
    FanController.gradient4(color1, color2, color3, color4)
    # await state.set_state(StateMachine.CUSTOM_PRESETS)
    print("".join(emojis))
    await state.update_data(GRADIENT4_COLOR="".join(emojis))
    await state.update_data(GRADIENT4_COLOR_TEXT=" ".join(colors))


@exception
@gradient4Router.callback_query(F.data == "favorite")
async def favorite(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Добавлено в избранное!")

    # Получаем состояние
    grad = await state.get_data()
    gradient = grad["GRADIENT4_COLOR"]
    color = grad["GRADIENT4_COLOR_TEXT"]

    # Открываем файл для чтения и загрузки текущих данных
    try:
        with open("./config/presets.json", "r") as presetFile:
            preset = json.load(presetFile)
    except FileNotFoundError:
        preset = {}  # Создаем пустой словарь, если файл отсутствует

    # Обновляем данные
    preset[gradient] = color

    # Сохраняем обновленные данные обратно в файл
    with open("./config/presets.json", "w") as presetFile:
        json.dump(preset, presetFile, indent=4)

    print("Файл успешно обновлён!")



@exception
@gradient4Router.message(StateFilter(StateMachine.GRADIENT4), F.text == names["make"])
async def make(message: Message, state: FSMContext):
    await state.set_state(StateMachine.GRADIENT4_1)
    await message.answer('Выбери 1-й цвет', reply_markup=colorKeyboard)

@exception
@gradient4Router.message(StateFilter(StateMachine.GRADIENT4_1), F.text.in_(names["colors"]["basicColors"].values()))
async def colorPick(message: Message, state: FSMContext):
    colorIndex = int(list(names["colors"]["basicColors"].values()).index(message.text))
    color = list(names["colors"]["basicColors"].keys())[colorIndex]
    logger.info(f"Выбран {color.capitalize()} для 4Gradient_1")

    await state.update_data(GRADIENT4_COLOR_1=f"{color.upper()}")
    await state.set_state(StateMachine.GRADIENT4_2)
    await message.answer(names["colors"]["basicColors"][f"{color}"] + ' установлен в качестве первого цвета для ' + names["custom"]["gradient4"] + '\nВыбери второй', reply_markup=colorKeyboard)

@exception
@gradient4Router.message(StateFilter(StateMachine.GRADIENT4_2), F.text.in_(names["colors"]["basicColors"].values()))
async def colorPick(message: Message, state: FSMContext):
    colorIndex = int(list(names["colors"]["basicColors"].values()).index(message.text))
    color = list(names["colors"]["basicColors"].keys())[colorIndex]
    logger.info(f"Выбран {color.capitalize()} для 4Gradient_2")

    await state.update_data(GRADIENT4_COLOR_2=f"{color.upper()}")
    await state.set_state(StateMachine.GRADIENT4_3)
    await message.answer(names["colors"]["basicColors"][f"{color}"] + ' установлен в качестве второго цвета для ' + names["custom"]["gradient4"] + '\nВыбери третий', reply_markup=colorKeyboard)

@exception
@gradient4Router.message(StateFilter(StateMachine.GRADIENT4_3), F.text.in_(names["colors"]["basicColors"].values()))
async def colorPick(message: Message, state: FSMContext):
    colorIndex = int(list(names["colors"]["basicColors"].values()).index(message.text))
    color = list(names["colors"]["basicColors"].keys())[colorIndex]
    logger.info(f"Выбран {color.capitalize()} для 4Gradient_3")

    await state.update_data(GRADIENT4_COLOR_3=f"{color.upper()}")
    await state.set_state(StateMachine.GRADIENT4_4)
    await message.answer(names["colors"]["basicColors"][f"{color}"] + ' установлен в качестве третьего цвета для ' + names["custom"]["gradient4"] + '\nВыбери четвёртый', reply_markup=colorKeyboard)



@exception
@gradient4Router.message(StateFilter(StateMachine.GRADIENT4_4), F.text.in_(names["colors"]["basicColors"].values()))
async def colorPick(message: Message, state: FSMContext):
    colorIndex = int(list(names["colors"]["basicColors"].values()).index(message.text))
    color = list(names["colors"]["basicColors"].keys())[colorIndex]
    logger.info(f"Выбран {color.capitalize()} для 4Gradient_4")

    await state.update_data(GRADIENT4_COLOR_4=f"{color.upper()}")
    await message.answer(names["colors"]["basicColors"][f"{color}"] + ' установлен в качестве четвёртого цвета для ' + names["custom"]["gradient4"])
    color = await state.get_data()
    # await state.update_data(GRADIENT4_COLOR=)
    color1 = color["GRADIENT4_COLOR_1"]
    color2 = color["GRADIENT4_COLOR_2"]
    color3 = color["GRADIENT4_COLOR_3"]
    color4 = color["GRADIENT4_COLOR_4"]
    emojis = [color1,color2,color3,color4]
    colors = [names["colors"]["basicColors"][x.lower()] for x in emojis]
    await state.update_data(GRADIENT4_COLOR="".join(colors))
    await state.update_data(GRADIENT4_COLOR_TEXT=" ".join(emojis))
    FanController.gradient4(color1, color2, color3, color4)
    await message.answer(texts["finalGradient"] + " ".join(colors),reply_markup=addToFavoritesKeyboard)
    await state.set_state(StateMachine.CUSTOM_PRESETS)
