from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import KeyboardButton, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from res.action_list_text import *
from res.info_text import *
from state.general_state import AppState
from state.info_state import InfoState

actionListHandler = Router()


@actionListHandler.message(default_state, F.text == CONTINUE_BUTTON_TEXT)
@actionListHandler.message(InfoState.waitPressButtons, F.text == CONTINUE_BUTTON_TEXT)
@actionListHandler.message(AppState.actionList, F.text == CONTINUE_BUTTON_TEXT)
async def actionListHandlerInit(message: Message, state: FSMContext) -> None:
    await state.set_state(AppState.actionList)

    keyboard = ReplyKeyboardBuilder().row(
        KeyboardButton(text=ENTER_PRODUCT_NAME_BUTTON_TEXT),
        KeyboardButton(text=ACTIVE_PURCHASE_BUTTON_TEXT)
    ).row(
        KeyboardButton(text=COMMON_ANALYSIS_BUTTON_TEXT),
        KeyboardButton(text=BALANCE_BUTTON_TEXT)
    ).row(
        KeyboardButton(text=BACK_BUTTON_TEXT)
    )

    await message.answer(text=ACTION_LIST_HELLO_TEXT, reply_markup=keyboard.as_markup(resize_keyboard=True))
