from aiogram.fsm.state import StatesGroup, State

# Определение классов состояний
class StateMachine(StatesGroup):
    START = State()
    CUSTOM_PRESETS = State()

    FADE_IN_OUT = State()