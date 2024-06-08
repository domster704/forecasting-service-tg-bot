from aiogram.fsm.state import StatesGroup, State


class AuthState(StatesGroup):
    login = State()
    password = State()
