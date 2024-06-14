"""
Раздел <Активные закупки>
"""

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from pagination import Pagination
from res.action_list_text import ACTIVE_PURCHASE_BUTTON_TEXT
from res.active_purchase_text import *
from res.general_text import BACK_BUTTON_TEXT, CALLBACK_DATA_PAGINATION_END
from state.active_purchase_state import ActivePurchaseState
from state.app_state import AppState

activePurchaseRouter = Router()


@activePurchaseRouter.message(AppState.activePurchase, F.text == ACTIVE_PURCHASE_BUTTON_TEXT)
@activePurchaseRouter.message(ActivePurchaseState.choosePurchase, F.text == ACTIVE_PURCHASE_BUTTON_TEXT)
async def activePurchaseInit(message: Message, state: FSMContext) -> None:
    await state.set_state(ActivePurchaseState.choosePurchase)

    keyboard = ReplyKeyboardBuilder().row(
        KeyboardButton(text=BACK_BUTTON_TEXT)
    )

    await message.answer(text=ACTIVE_PURCHASE_HELLO_TEXT, reply_markup=keyboard.as_markup(resize_keyboard=True))

    items = [
        "Пылесос синий",
        "Шторы рулонные",
        "Удлинитель 5 м",
        "Пилот на 5 гнезд",
        "Пилот на 6 гнезд",
        "Пилот на 7 гнезд",
        "Пилот на 8 гнезд",
        "Пилот на 9 гнезд",
        "Пилот на 10 гнезд",
        "Пилот на 11 гнезд",
        "Пилот на 12 гнезд",
        "Пилот на 13 гнезд",
        "Пилот на 14 гнезд",
        "Пилот на 15 гнезд",
        "Пилот на 16 гнезд",
        "Пилот на 17 гнезд",
        "Пилот на 18 гнезд",
    ]
    CALLBACK_DATA_PAGINATION_END = "active_purchase"
    pagination: Pagination = Pagination(
        items=items,
    )
    await state.update_data(pagination=pagination)
    await message.answer(**pagination.getMessageData())

