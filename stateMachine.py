from aiogram.fsm.state import StatesGroup, State

# Определение классов состояний
class StateMachine(StatesGroup):
    START = State()
    CUSTOM_PRESETS = State()

    FADE_IN_OUT = State()

    COLOR_1 = State()
    COLOR_WIPE_1 = State()
    COLOR_WIPE_2 = State()