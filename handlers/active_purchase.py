"""
Раздел <Активные закупки>
"""

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from res.info_text import *
from state.app_state import AppState

activePurchaseRouter = Router()


@activePurchaseRouter.message(AppState.activePurchase, F.text == CONTINUE_BUTTON_TEXT)
async def activePurchaseInit(message: Message, state: FSMContext) -> None:
    await state.set_state(AppState.activePurchase)

    keyboard = ReplyKeyboardBuilder().row(
        KeyboardButton(text=BACK_BUTTON_TEXT)
    )

    await message.answer(text=PRODUCT_HELLO_TEXT, reply_markup=keyboard.as_markup(resize_keyboard=True))
