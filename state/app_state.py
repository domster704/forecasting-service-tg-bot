from aiogram.fsm.state import StatesGroup, State


class AppState(StatesGroup):
    """
    Класс состояния приложения, где каждое состояние - это используемый handler на данный момент
    """
    login = State()  # шаг авторизации
    info = State()  # шаг информации о пользователе и о помощи
    actionList = State()  # шаг общего списка действий
    product = State()  # шаг создания закупки
    commonPurchaseAnalysis = State()  # шаг общего анализа закупки
    balanceState = State()  # шаг баланса
