"""
Раздел <Закупка>
"""

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from handlers.product_handler import productActionsInit
from res.general_text import SOMETHING_WRONG
from res.product_text import *
from state.product_state import ProductState

createPurchaseRouter = Router()


@createPurchaseRouter.message(ProductState.waitPurchaseActions, F.text == PURCHASE_PRODUCT_BUTTON_TEXT)
@createPurchaseRouter.message(ProductState.productWaitActions, F.text == PURCHASE_PRODUCT_BUTTON_TEXT)
async def purchaseProductInit(message: Message, state: FSMContext) -> None:
    await state.set_state(ProductState.waitPurchaseActions)

    keyboard = ReplyKeyboardBuilder().add(
        KeyboardButton(text=CREATE_BUTTON_TEXT),
        KeyboardButton(text=EDIT_BUTTON_TEXT),
    ).row(
        KeyboardButton(text=BACK_BUTTON_TEXT),
    )

    await message.answer(text=CREATE_PURCHASE_INIT_MESSAGE_TEXT, reply_markup=keyboard.as_markup(resize_keyboard=True))


@createPurchaseRouter.message(ProductState.waitPurchaseActions, F.text == EDIT_BUTTON_TEXT)
async def editPurchase(message: Message, state: FSMContext) -> None:
    if 'purchase' not in (await state.get_data()).keys():
        await message.answer(text=WRONG_EDIT_PURCHASE_BECAUSE_NONE)
        return

    purchase: PurchaseProduct = (await state.get_data())['purchase']
    await message.answer(text=PURCHASE_EDIT_SUCCESS_MESSAGE_TEXT(purchase.__str__()))
    await createPurchase(message, state)


@createPurchaseRouter.message(ProductState.waitPurchaseActions, F.text == CREATE_BUTTON_TEXT)
async def createPurchase(message: Message, state: FSMContext) -> None:
    await state.set_state(ProductState.cretePurchase)
    await message.answer(text=INPUT_PRODUCT_AMOUNT_TEXT, reply_markup=ReplyKeyboardRemove())


@createPurchaseRouter.message(ProductState.cretePurchase)
async def inputProductAmount(message: Message, state: FSMContext) -> None:
    try:
        productAmount: int = int(message.text)
        await state.update_data(product_amount=productAmount)
        await state.set_state(ProductState.inputSubAccount)

        await message.answer(text=INPUT_SUB_ACCOUNT_TEXT)
    except Exception as e:
        await message.answer(text=SOMETHING_WRONG)
        print(e)


@createPurchaseRouter.message(ProductState.inputSubAccount)
async def inputProductAmount(message: Message, state: FSMContext) -> None:
    subAccount: str = message.text
    await state.update_data(sub_account=subAccount)

    purchaseProduct = PurchaseProduct(**(await state.get_data()))
    await state.update_data(purchase=purchaseProduct)

    await message.answer(text=PURCHASE_CREATE_SUCCESS_MESSAGE_TEXT(purchaseProduct.__str__()))

    await state.set_state(ProductState.productActions)
    await productActionsInit(message, state)


class PurchaseProduct:
    def __init__(self, product_amount: int, sub_account: str, **kwargs):
        self.productAmount = product_amount
        self.subAccount = sub_account

    def __str__(self):
        return f"{self.productAmount} {self.subAccount}"
