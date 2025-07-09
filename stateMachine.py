from aiogram.fsm.state import StatesGroup, State

# Определение классов состояний
class StateMachine(StatesGroup):
    START = State()
    CUSTOM_PRESETS = State()

    COLOR_FADE_IN_OUT = State()
    TIME_FADE_IN_OUT = State()
    FADE_IN_OUT = State()

    COLOR_1_COLOR_WIPE = State()
    COLOR_WIPE_1 = State()
    COLOR_WIPE_2 = State()