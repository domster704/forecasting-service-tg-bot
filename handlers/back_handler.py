"""
Раздел с кнопками Назад для возврата на предыдущий шаг/этап
"""

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message

from handlers.actions_list_handler import actionListHandlerInit
from handlers.info_handler import infoHandlerInit
from handlers.product_handler import productInit, productActionsInit
from res.general_text import BACK_BUTTON_TEXT
from state.app_state import AppState
from state.info_state import InfoState
from state.product_state import ProductState

backRouter = Router()


@backRouter.message(default_state, F.text == BACK_BUTTON_TEXT)
@backRouter.message(InfoState.userInfo, F.text == BACK_BUTTON_TEXT)
@backRouter.message(AppState.info, F.text == BACK_BUTTON_TEXT)
async def backActionUserInfo(message: Message, state: FSMContext) -> None:
    """
    Кнопка назад в блоке <Информация о пользователе и помощь>.
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


@backRouter.message(AppState.commonPurchaseAnalysis, F.text == BACK_BUTTON_TEXT)
async def backButtonGeneralPurchaseAnalysis(message: Message, state: FSMContext) -> None:
    """
    Кнопка назад в блоке <Общий анализ закупок>
    :param message:
    :param state:
    :return:
    """
    await state.set_state(AppState.actionList)
    await actionListHandlerInit(message, state)


@backRouter.message(AppState.balanceState, F.text == BACK_BUTTON_TEXT)
async def backButtonBalance(message: Message, state: FSMContext) -> None:
    """
    Кнопка назад в блоке <Общий анализ закупок>
    :param message:
    :param state:
    :return:
    """
    await state.set_state(AppState.actionList)
    await actionListHandlerInit(message, state)


@backRouter.message(ProductState.productName, F.text == BACK_BUTTON_TEXT)
async def backButtonProductName(message: Message, state: FSMContext) -> None:
    """
    Кнопка назад в блоке <Товар>:`ввод имени товара`
    :param message:
    :param state:
    :return:
    """
    await state.set_state(AppState.actionList)
    await actionListHandlerInit(message, state)


@backRouter.message(ProductState.productNameSuggestedList, F.text == BACK_BUTTON_TEXT)
@backRouter.message(ProductState.enterProductNumFromList, F.text == BACK_BUTTON_TEXT)
async def backButtonProductSuggestedList(message: Message, state: FSMContext) -> None:
    """
    Кнопка назад в блоке <Товар>:`список товаров с пагинацией`
    :param message:
    :param state:
    :return:
    """
    await state.set_state(AppState.product)
    await productInit(message, state)


@backRouter.message(ProductState.productWaitActions, F.text == BACK_BUTTON_TEXT)
@backRouter.message(ProductState.productActions, F.text == BACK_BUTTON_TEXT)
async def backButtonProductActions(message: Message, state: FSMContext) -> None:
    """
    Кнопка назад в блоке <Товар>:`список товаров с пагинацией`
    :param message:
    :param state:
    :return:
    """
    await state.set_state(ProductState.productNameSuggestedList)
    await productInit(message, state)


@backRouter.message(ProductState.choosePeriod, F.text == BACK_BUTTON_TEXT)
async def backButtonProductActions(message: Message, state: FSMContext) -> None:
    """
    Кнопка назад в блоке <Товар>:`список действий с товаром`
    :param message:
    :param state:
    :return:
    """
    await state.set_state(ProductState.productNameSuggestedList)
    await productActionsInit(message, state)
