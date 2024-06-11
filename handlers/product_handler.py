"""
Раздел <Товар>
"""

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, ReplyKeyboardRemove, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from pagination import Pagination
from res.action_list_text import ENTER_PRODUCT_NAME_BUTTON_TEXT
from res.general_text import BACK_BUTTON_TEXT
from res.product_text import PRODUCT_HELLO_TEXT, CALLBACK_DATA_PRODUCT_END, INPUT_WRONG_INDEX
from state.app_state import AppState
from state.product_state import ProductState

productRouter = Router()


@productRouter.message(default_state, F.text == ENTER_PRODUCT_NAME_BUTTON_TEXT)
@productRouter.message(AppState.actionList, F.text == ENTER_PRODUCT_NAME_BUTTON_TEXT)
@productRouter.message(AppState.product, F.text == ENTER_PRODUCT_NAME_BUTTON_TEXT)
async def productInit(message: Message, state: FSMContext) -> None:
    await state.set_state(ProductState.productName)

    keyboard = ReplyKeyboardBuilder().row(
        KeyboardButton(text=BACK_BUTTON_TEXT)
    )

    await message.answer(text=PRODUCT_HELLO_TEXT, reply_markup=keyboard.as_markup(resize_keyboard=True))


@productRouter.message(ProductState.productName, F.text != BACK_BUTTON_TEXT)
async def enterProductName(message: Message, state: FSMContext) -> None:
    productName: str = message.text
    await state.update_data(productName=productName)
    print(productName)

    await state.set_state(ProductState.productNameSuggestedList)
    await showProductNameSuggestedList(message, state)


@productRouter.message(ProductState.productNameSuggestedList, F.text != BACK_BUTTON_TEXT)
async def showProductNameSuggestedList(message: Message, state: FSMContext) -> None:
    keyboard = ReplyKeyboardBuilder().row(
        KeyboardButton(text=BACK_BUTTON_TEXT)
    )

    items = [
        "Пылесос синий",
        "Шторы рулонные",
        "Удлинитель 5 м",
        "Пилот на 5 гнезд",
        "Пилот на 6 гнезд",
        "Пилот на 7 гнезд",
        "Пилот на 8 гнезд",
    ]
    pagination: Pagination = Pagination(
        items=items,
        callback_data_end=CALLBACK_DATA_PRODUCT_END,
    )

    await state.update_data(pagination=pagination)
    await message.answer(**pagination.getMessageData())
    await state.set_state(ProductState.enterProductNumFromList)


@productRouter.message(ProductState.enterProductNumFromList, F.text != BACK_BUTTON_TEXT)
async def getProductFromList(message: Message, state: FSMContext) -> None:
    try:
        index = int(message.text) - 1
        pagination: Pagination = (await state.get_data())["pagination"]
        print(pagination.items[index])
        await message.reply(text=pagination.items[index], reply_markup=ReplyKeyboardRemove())
    except Exception as e:
        print(e)
        await message.reply(text=INPUT_WRONG_INDEX)


@productRouter.callback_query(F.data == f"{Pagination.CALLBACK_DATA_START_NEXT}{CALLBACK_DATA_PRODUCT_END}")
async def nextPageProduct(callback: types.CallbackQuery, state: FSMContext) -> None:
    pagination: Pagination = (await state.get_data())["pagination"]
    await callback.message.edit_text(**pagination
                                     .nextPage()
                                     .getMessageData())


@productRouter.callback_query(F.data == f"{Pagination.CALLBACK_DATA_START_PREV}{CALLBACK_DATA_PRODUCT_END}")
async def nextPageProduct(callback: types.CallbackQuery, state: FSMContext) -> None:
    pagination: Pagination = (await state.get_data())["pagination"]
    await callback.message.edit_text(**pagination
                                     .prevPage()
                                     .getMessageData())
