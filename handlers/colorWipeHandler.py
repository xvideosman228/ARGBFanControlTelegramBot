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

colorWipeRouter = Router()



@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_1), F.text == names["colors"]["basicColors"]["red"])
async def red(message: Message, state: FSMContext):
    logger.info("Выбран Red для Color Wipe")
    await state.update_data({StateMachine.COLOR_1:"red"})
    await message.answer(names["colors"]["basicColors"]["red"] + ' для ' + names["custom"]["colorwipe"])
    for x in names["colors"]["basicColors"]:
        print(f"""
@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_2), F.text == names["colors"]["basicColors"]["{x}"])
async def {x}(message: Message, state: FSMContext):
    logger.info("Выбран {x.capitalize()} для Color Wipe")
    await message.answer(names["colors"]["basicColors"]["{x}"] + ' для ' + names["custom"]["colorwipe"])
    FanController.colorwipe(await state.get_data()["COLOR_1"], '{x.upper()}')
    """)

'''
@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_1), F.text == names["colors"]["basicColors"]["red"])
async def red(message: Message, state: FSMContext):
    logger.info("Выбран Red для Color Wipe")
    await state.update_data({StateMachine.COLOR_1:"red"})
    await state.set_state(StateMachine.COLOR_WIPE_2)
    await message.answer(names["colors"]["basicColors"]["red"] + ' для ' + names["custom"]["colorwipe"])

'''

@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_1), F.text == names["colors"]["basicColors"]["green"])
async def green(message: Message, state: FSMContext):
    logger.info("Выбран Green для Color Wipe")
    await state.update_data({StateMachine.COLOR_1:"green"})
    print("green")
    await state.set_state(StateMachine.COLOR_WIPE_2)
    await message.answer(names["colors"]["basicColors"]["green"] + ' для ' + names["custom"]["colorwipe"])


@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_1), F.text == names["colors"]["basicColors"]["blue"])
async def blue(message: Message, state: FSMContext):
    logger.info("Выбран Blue для Color Wipe")
    await state.update_data({StateMachine.COLOR_1:"blue"})
    await state.set_state(StateMachine.COLOR_WIPE_2)
    await message.answer(names["colors"]["basicColors"]["blue"] + ' для ' + names["custom"]["colorwipe"])


@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_1), F.text == names["colors"]["basicColors"]["yellow"])
async def yellow(message: Message, state: FSMContext):
    logger.info("Выбран Yellow для Color Wipe")
    await state.update_data({StateMachine.COLOR_1:"yellow"})
    await state.set_state(StateMachine.COLOR_WIPE_2)
    await message.answer(names["colors"]["basicColors"]["yellow"] + ' для ' + names["custom"]["colorwipe"])


@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_1), F.text == names["colors"]["basicColors"]["yelloworange"])
async def yelloworange(message: Message, state: FSMContext):
    logger.info("Выбран Yelloworange для Color Wipe")
    await state.update_data(COLOR_1="yelloworange")
    await state.set_state(StateMachine.COLOR_WIPE_2)
    await message.answer(names["colors"]["basicColors"]["yelloworange"] + ' для ' + names["custom"]["colorwipe"])


@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_1), F.text == names["colors"]["basicColors"]["orange"])
async def orange(message: Message, state: FSMContext):
    logger.info("Выбран Orange для Color Wipe")
    await state.update_data({StateMachine.COLOR_1:"orange"})
    await state.set_state(StateMachine.COLOR_WIPE_2)
    await message.answer(names["colors"]["basicColors"]["orange"] + ' для ' + names["custom"]["colorwipe"])


@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_1), F.text == names["colors"]["basicColors"]["orangered"])
async def orangered(message: Message, state: FSMContext):
    logger.info("Выбран Orangered для Color Wipe")
    await state.update_data({StateMachine.COLOR_1:"orangered"})
    await state.set_state(StateMachine.COLOR_WIPE_2)
    await message.answer(names["colors"]["basicColors"]["orangered"] + ' для ' + names["custom"]["colorwipe"])


@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_1), F.text == names["colors"]["basicColors"]["lightblue"])
async def lightblue(message: Message, state: FSMContext):
    logger.info("Выбран Lightblue для Color Wipe")
    await state.update_data({StateMachine.COLOR_1:"lightblue"})
    await state.set_state(StateMachine.COLOR_WIPE_2)
    await message.answer(names["colors"]["basicColors"]["lightblue"] + ' для ' + names["custom"]["colorwipe"])


@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_1), F.text == names["colors"]["basicColors"]["darkblue"])
async def darkblue(message: Message, state: FSMContext):
    logger.info("Выбран Darkblue для Color Wipe")
    await state.update_data({StateMachine.COLOR_1:"darkblue"})
    await state.set_state(StateMachine.COLOR_WIPE_2)
    await message.answer(names["colors"]["basicColors"]["darkblue"] + ' для ' + names["custom"]["colorwipe"])


@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_1), F.text == names["colors"]["basicColors"]["violet"])
async def violet(message: Message, state: FSMContext):
    logger.info("Выбран Violet для Color Wipe")
    await state.update_data({StateMachine.COLOR_1:"violet"})
    await state.set_state(StateMachine.COLOR_WIPE_2)
    await message.answer(names["colors"]["basicColors"]["violet"] + ' для ' + names["custom"]["colorwipe"])


@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_1), F.text == names["colors"]["basicColors"]["white"])
async def white(message: Message, state: FSMContext):
    logger.info("Выбран White для Color Wipe")
    await state.update_data({StateMachine.COLOR_1:"white"})
    await state.set_state(StateMachine.COLOR_WIPE_2)
    await message.answer(names["colors"]["basicColors"]["white"] + ' для ' + names["custom"]["colorwipe"])


@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_2), F.text == names["colors"]["basicColors"]["red"])
async def red(message: Message, state: FSMContext):
    logger.info("Выбран Red для Color Wipe 2")
    await message.answer(names["colors"]["basicColors"]["red"] + ' для ' + names["custom"]["colorwipe"])
    FanController.colorwipe(await state.get_data()["COLOR_1"], 'RED')


@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_2), F.text == names["colors"]["basicColors"]["green"])
async def green(message: Message, state: FSMContext):
    logger.info("Выбран Green для Color Wipe 2")
    await message.answer(names["colors"]["basicColors"]["green"] + ' для ' + names["custom"]["colorwipe"])
    FanController.colorwipe(await state.get_data()["COLOR_1"], 'GREEN')


@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_2), F.text == names["colors"]["basicColors"]["blue"])
async def blue(message: Message, state: FSMContext):
    logger.info("Выбран Blue для Color Wipe 2")
    await message.answer(names["colors"]["basicColors"]["blue"] + ' для ' + names["custom"]["colorwipe"])
    FanController.colorwipe(await state.get_data()["COLOR_1"], 'BLUE')


@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_2), F.text == names["colors"]["basicColors"]["yellow"])
async def yellow(message: Message, state: FSMContext):
    logger.info("Выбран Yellow для Color Wipe 2")
    await message.answer(names["colors"]["basicColors"]["yellow"] + ' для ' + names["custom"]["colorwipe"])
    FanController.colorwipe(await state.get_data()["COLOR_1"], 'YELLOW')


@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_2),F.text == names["colors"]["basicColors"]["yelloworange"])
async def yelloworange(message: Message, state: FSMContext):
    logger.info("Выбран Yelloworange для Color Wipe 2")
    await message.answer(names["colors"]["basicColors"]["yelloworange"] + ' для ' + names["custom"]["colorwipe"])
    color1 = await state.get_data()["COLOR_1"]
    print(color1)
    FanController.colorwipe(color1, 'YELLOWORANGE')


@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_2), F.text == names["colors"]["basicColors"]["orange"])
async def orange(message: Message, state: FSMContext):
    logger.info("Выбран Orange для Color Wipe 2")
    await message.answer(names["colors"]["basicColors"]["orange"] + ' для ' + names["custom"]["colorwipe"])
    FanController.colorwipe(await state.get_data()["COLOR_1"], 'ORANGE')


@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_2), F.text == names["colors"]["basicColors"]["orangered"])
async def orangered(message: Message, state: FSMContext):
    logger.info("Выбран Orangered для Color Wipe 2")
    await message.answer(names["colors"]["basicColors"]["orangered"] + ' для ' + names["custom"]["colorwipe"])
    FanController.colorwipe(await state.get_data()["COLOR_1"], 'ORANGERED')


@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_2), F.text == names["colors"]["basicColors"]["lightblue"])
async def lightblue(message: Message, state: FSMContext):
    logger.info("Выбран Lightblue для Color Wipe 2")
    await message.answer(names["colors"]["basicColors"]["lightblue"] + ' для ' + names["custom"]["colorwipe"])
    FanController.colorwipe(await state.get_data()["COLOR_1"], 'LIGHTBLUE')


@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_2), F.text == names["colors"]["basicColors"]["darkblue"])
async def darkblue(message: Message, state: FSMContext):
    logger.info("Выбран Darkblue для Color Wipe 2")
    await message.answer(names["colors"]["basicColors"]["darkblue"] + ' для ' + names["custom"]["colorwipe"])
    FanController.colorwipe(await state.get_data()["COLOR_1"], 'DARKBLUE')


@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_2), F.text == names["colors"]["basicColors"]["violet"])
async def violet(message: Message, state: FSMContext):
    logger.info("Выбран Violet для Color Wipe 2")
    await message.answer(names["colors"]["basicColors"]["violet"] + ' для ' + names["custom"]["colorwipe"])
    color1 = await state.get_data()
    print(color1)
    FanController.colorwipe(color1["COLOR_1"].upper(), 'VIOLET')


@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_2), F.text == names["colors"]["basicColors"]["white"])
async def white(message: Message, state: FSMContext):
    logger.info("Выбран White для Color Wipe 2")
    await message.answer(names["colors"]["basicColors"]["white"] + ' для ' + names["custom"]["colorwipe"])
    FanController.colorwipe(await state.get_data()["COLOR_1"], 'WHITE')


@exception
@colorWipeRouter.message(StateFilter(StateMachine.COLOR_WIPE_2))
async def colorChoose(message: Message, state: FSMContext):
    logger.info("Открыто меню выбора цвета для Color Wipe 2")
    await message.answer(texts["chooseColor"], reply_markup=colorKeyboard)


"""
    "fire": "\uD83D\uDD25 огонь",
    "ocean": "\uD83C\uDF0A океан"
"""