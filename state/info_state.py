from aiogram.fsm.state import StatesGroup, State


class InfoState(StatesGroup):
    waitPressButtons = State()
    userInfo = State()
    assertError = State()
