from typing import Callable

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, default_state
from aiogram.types import Message

from handlers.info import infoHandlerInit
from res.general_text import BACK_BUTTON_TEXT
from state.general_state import AppState
from state.info_state import InfoState

backRouter = Router()


class StateData(object):
    def __init__(self, state: State, handler: Callable):
        self.state = state
        self.handler = handler


history_tree = {
    "InfoState:userInfo": StateData(AppState.info, infoHandlerInit),
}


@backRouter.message(default_state, F.text == BACK_BUTTON_TEXT)
@backRouter.message(InfoState.userInfo, F.text == BACK_BUTTON_TEXT)
async def backActionUserInfo(message: Message, state: FSMContext) -> None:
    """
    Кнопка назад в блоке <Информация о пользователе>.
    Используется по умолчанию, если есть только default_state
    :param message:
    :param state:
    :return:
    """
    await state.set_state(AppState.info)
    await infoHandlerInit(message, state)


@backRouter.message(AppState.actionList, F.text == BACK_BUTTON_TEXT)
async def backButtonActionList(message: Message, state: FSMContext) -> None:
    """
    Кнопка назад в блоке <Список основных действий>
    :param message:
    :param state:
    :return:
    """
    await state.set_state(AppState.info)
    await infoHandlerInit(message, state)
