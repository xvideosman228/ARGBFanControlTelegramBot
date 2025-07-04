from aiogram.fsm.state import StatesGroup, State

# Определение классов состояний
class StateMachine(StatesGroup):
    START = State()
    FAN_CONFIG = State()
    ABOUT = State()