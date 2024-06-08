from aiogram.fsm.state import StatesGroup, State


class AppState(StatesGroup):
    start = State()
    login = State()
    info = State()
    createPurchase = State()
