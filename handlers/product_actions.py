"""
Раздел <Товар>
"""
import aiohttp
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, KeyboardButton, BufferedInputFile
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config import apiURL, bot
from db.db_utils import getUserCookies
from res.general_text import *
from res.product_text import *
from state.product_state import ProductState
from utils import base64ToBufferInputStream


class ProductActions:
    @staticmethod
    async def checkRegular(message, product_name: str) -> bool | None:
        async with aiohttp.ClientSession(cookies=await getUserCookies(message.chat.id)) as session:
            async with session.get(f"{apiURL}/search/regular", params={
                "user_pick": product_name
            }) as r:
                print(await r.text(), r.status)
                if r.status == 200:
                    res = await r.json()
                    return res['is_regular']

                return None

    @staticmethod
    async def suggestPrice(message, period, price_amount_type) -> bytes:
        async with aiohttp.ClientSession(cookies=await getUserCookies(message.chat.id)) as session:
            async with session.get(f"{apiURL}/search/purchase_stats", params={
                "period": period,
                "summa": str(price_amount_type)
            }) as r:
                res = await r.json()
                if res['state'] != 'Success':
                    return b''

                return base64ToBufferInputStream(res['plot_image'])


productActionsRouter = Router()


@productActionsRouter.message(ProductState.productActions)
async def productActionsInit(message: Message, state: FSMContext) -> None:
    await state.set_state(ProductState.productWaitActions)

    stateData = await state.get_data()

    productName: str = stateData["productName"]
    regularity: bool = stateData['regularity'] \
        if 'regularity' in stateData.keys() \
        else await ProductActions.checkRegular(message, productName)

    keyboard = ReplyKeyboardBuilder()
    first_row = [KeyboardButton(text=ANALYZE_PRODUCT_BUTTON_TEXT),
                 KeyboardButton(text=SUGGESTED_PRODUCT_BUTTON_TEXT)] \
        if regularity else [KeyboardButton(text=ANALYZE_PRODUCT_BUTTON_TEXT)]

    keyboard.row(
        *first_row
    ).row(
        KeyboardButton(text=PURCHASE_PRODUCT_BUTTON_TEXT),
        KeyboardButton(text=BACK_BUTTON_TEXT)
    )

    await state.update_data(regularity=regularity)
    await message.answer(
        text=PRODUCT_ACTIONS_TEXT(productName, regularity),
        reply_markup=keyboard.as_markup(resize_keyboard=True))


@productActionsRouter.message(ProductState.productWaitActions, F.text == SUGGESTED_PRODUCT_BUTTON_TEXT,
                              flags={"rights": "permission_suggestion"})
async def predictProduct(message: Message, state: FSMContext) -> None:
    keyboard = ReplyKeyboardBuilder().row(
        KeyboardButton(text=YEAR_TEXT),
        KeyboardButton(text=QUARTER_TEXT),
        KeyboardButton(text=MONTH_TEXT),
    ).row(
        KeyboardButton(text=BACK_BUTTON_TEXT)
    )

    await state.set_state(ProductState.choosePeriod)
    await message.answer(text=CHOSE_PERIOD_TEXT, reply_markup=keyboard.as_markup(resize_keyboard=True))


@productActionsRouter.message(ProductState.choosePeriod, F.text == YEAR_TEXT)
@productActionsRouter.message(ProductState.choosePeriod, F.text == QUARTER_TEXT)
@productActionsRouter.message(ProductState.choosePeriod, F.text == MONTH_TEXT)
async def predictProductByPeriod(message: Message, state: FSMContext) -> None:
    await message.answer(text=SELECT_PERIOD_TEXT(message.text))

    period: int = 1
    if message.text == YEAR_TEXT:
        period = 1
    elif message.text == QUARTER_TEXT:
        period = 2
    elif message.text == MONTH_TEXT:
        period = 3

    price = await ProductActions.suggestPrice(message, period, True)
    amount = await ProductActions.suggestPrice(message, period, False)

    await bot.send_photo(message.chat.id,
                         photo=BufferedInputFile(price, filename="price.png"))
    await bot.send_photo(message.chat.id,
                         photo=BufferedInputFile(amount, filename="amount.png"))
