from aiogram.fsm.state import StatesGroup, State

# Определение классов состояний
class StateMachine(StatesGroup):
    START = State()
    CUSTOM_PRESETS = State()

    COLOR_FADE_IN_OUT = State()
    TIME_FADE_IN_OUT = State()
    FADE_IN_OUT = State()

    COLOR_1_COLOR_WIPE = State()
    COLOR_2_COLOR_WIPE = State()
    COLOR_WIPE_1 = State()
    COLOR_WIPE_2 = State()
    COLOR_WIPE_TIME = State()

    GRADIENT_1 = State()
    GRADIENT_2 = State()
    GRADIENT_COLOR_1 = State()
    GRADIENT_COLOR_2 = State()

    SMOOTH_GRADIENT_1 = State()
    SMOOTH_GRADIENT_2 = State()
    SMOOTH_GRADIENT_COLOR_1 = State()
    SMOOTH_GRADIENT_COLOR_2 = State()

    GRADIENT4_1 = State()
    GRADIENT4_2 = State()
    GRADIENT4_3 = State()
    GRADIENT4_4 = State()
    GRADIENT4_COLOR_1 = State()
    GRADIENT4_COLOR_2 = State()
    GRADIENT4_COLOR_3 = State()
    GRADIENT4_COLOR_4 = State()

    CYLON = State()

