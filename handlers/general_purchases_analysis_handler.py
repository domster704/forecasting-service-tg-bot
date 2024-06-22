"""
Раздел <Общий анализ закупок>
"""
import aiohttp
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import KeyboardButton, Message, BufferedInputFile
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config import bot, apiURL_ML
from db.db import User
from db.db_utils import getUser
from res.general_actions_text import COMMON_ANALYSIS_BUTTON_TEXT
from res.general_purchases_analysis_text import *
from res.general_text import *
from state.app_state import AppState
from state.general_purchase_analysis_state import CommonPurchaseAnalysisState
from utils import base64ToBufferInputStream


class GeneralPurchaseAnalysis(object):
    @staticmethod
    async def allStatistics(message: Message, period, price):
        user: User = await getUser(message.chat.id)
        async with aiohttp.ClientSession(cookies=user.cookies) as session:
            async with session.get(f"{apiURL_ML}/v1/ml/analytics_all/purchase_stats", params={
                "period": period,
                "summa": str(price),
            }) as r:
                res = await r.json()

                if res['state'] != 'Success':
                    return b''

                return base64ToBufferInputStream(res['plot_image'])

    @staticmethod
    async def allHistoryAnalysis(message: Message, n: int):
        user: User = await getUser(message.chat.id)
        async with aiohttp.ClientSession(cookies=user.cookies) as session:
            async with session.get(f"{apiURL_ML}/v1/ml/analytics_all/history", params={
                "n": n,
            }) as r:
                res = await r.json()

                if r.status != 200:
                    return b''

                return base64ToBufferInputStream(res['file'])


commonPurchasesAnalysisRouter = Router()


@commonPurchasesAnalysisRouter.message(default_state, F.text == COMMON_ANALYSIS_BUTTON_TEXT,
                                       flags={"rights": "analysis_common"})
@commonPurchasesAnalysisRouter.message(AppState.generalActionsState, F.text == COMMON_ANALYSIS_BUTTON_TEXT,
                                       flags={"rights": "analysis_common"})
@commonPurchasesAnalysisRouter.message(AppState.commonPurchaseAnalysis, F.text == COMMON_ANALYSIS_BUTTON_TEXT,
                                       flags={"rights": "analysis_common"})
async def commonPurchaseAnalysisInit(message: Message, state: FSMContext) -> None:
    await state.set_state(AppState.commonPurchaseAnalysis)

    keyboard = ReplyKeyboardBuilder().row(
        KeyboardButton(text=PURCHASES_STATISTIC_BUTTON_TEXT),
        KeyboardButton(text=TOP_EXPENSIVE_BUTTON_TEXT)
    ).row(
        KeyboardButton(text=BACK_BUTTON_TEXT)
    )

    await message.answer(text=COMMON_PURCHASES_STATISTIC_HELLO_TEXT,
                         reply_markup=keyboard.as_markup(resize_keyboard=True))


@commonPurchasesAnalysisRouter.message(AppState.commonPurchaseAnalysis, F.text == TOP_EXPENSIVE_BUTTON_TEXT)
async def purchaseTopExpensiveEnterN(message: Message, state: FSMContext) -> None:
    keyboard = ReplyKeyboardBuilder().row(
        KeyboardButton(text=BACK_BUTTON_TEXT)
    )

    await state.set_state(CommonPurchaseAnalysisState.enterN)
    await message.answer(text=ENTER_N_EXPENSIVE_PURCHASES_MESSAGE_TEXT,
                         reply_markup=keyboard.as_markup(resize_keyboard=True))


@commonPurchasesAnalysisRouter.message(CommonPurchaseAnalysisState.enterN, F.text != BACK_BUTTON_TEXT)
async def purchaseTopExpensiveShowExcelFile(message: Message, state: FSMContext) -> None:
    try:
        n: int = int(message.text)
        allHistoryAnalysis = await GeneralPurchaseAnalysis.allHistoryAnalysis(message, n)

        await bot.send_document(message.chat.id,
                                document=BufferedInputFile(allHistoryAnalysis, filename="all_history.xlsx"))
    except Exception as e:
        await message.answer(text=SOMETHING_WRONG)


@commonPurchasesAnalysisRouter.message(AppState.commonPurchaseAnalysis, F.text == PURCHASES_STATISTIC_BUTTON_TEXT)
async def suggestProduct(message: Message, state: FSMContext) -> None:
    keyboard = ReplyKeyboardBuilder().row(
        KeyboardButton(text=YEAR_TEXT),
        KeyboardButton(text=QUARTER_TEXT),
        KeyboardButton(text=MONTH_TEXT),
    ).row(
        KeyboardButton(text=BACK_BUTTON_TEXT)
    )

    await state.set_state(CommonPurchaseAnalysisState.choosePeriod)
    await message.answer(text=CHOSE_PERIOD_TEXT, reply_markup=keyboard.as_markup(resize_keyboard=True))


@commonPurchasesAnalysisRouter.message(CommonPurchaseAnalysisState.choosePeriod, F.text == YEAR_TEXT)
@commonPurchasesAnalysisRouter.message(CommonPurchaseAnalysisState.choosePeriod, F.text == QUARTER_TEXT)
@commonPurchasesAnalysisRouter.message(CommonPurchaseAnalysisState.choosePeriod, F.text == MONTH_TEXT)
async def suggestProductYear(message: Message, state: FSMContext) -> None:
    await state.set_state(CommonPurchaseAnalysisState.chooseStatisticType)

    keyboard = ReplyKeyboardBuilder().add(
        KeyboardButton(text=AMOUNT_OF_PURCHASES_BUTTON_TEXT),
        KeyboardButton(text=PRICE_OF_PURCHASES_BUTTON_TEXT),
    ).row(
        KeyboardButton(text=BACK_BUTTON_TEXT)
    )

    period: int = 0
    if message.text == YEAR_TEXT:
        period = 1
    elif message.text == QUARTER_TEXT:
        period = 2
    elif message.text == MONTH_TEXT:
        period = 3

    await state.update_data(allPurchaseAnalysis_period=period)
    await message.answer(text=CHOSE_TYPE_TEXT, reply_markup=keyboard.as_markup(resize_keyboard=True))


@commonPurchasesAnalysisRouter.message(CommonPurchaseAnalysisState.chooseStatisticType,
                                       F.text == AMOUNT_OF_PURCHASES_BUTTON_TEXT)
async def suggestProductYear(message: Message, state: FSMContext) -> None:
    period: int = (await state.get_data())['allPurchaseAnalysis_period']
    allStatisticsAmount = await GeneralPurchaseAnalysis.allStatistics(message, period, False)

    await bot.send_photo(message.chat.id,
                         photo=BufferedInputFile(allStatisticsAmount, filename="amount.png"))


@commonPurchasesAnalysisRouter.message(CommonPurchaseAnalysisState.chooseStatisticType,
                                       F.text == PRICE_OF_PURCHASES_BUTTON_TEXT)
async def suggestProductYear(message: Message, state: FSMContext) -> None:
    period: int = (await state.get_data())['allPurchaseAnalysis_period']
    allStatisticsPrice = await GeneralPurchaseAnalysis.allStatistics(message, period, True)

    await bot.send_photo(message.chat.id,
                         photo=BufferedInputFile(allStatisticsPrice, filename="price.png"))
