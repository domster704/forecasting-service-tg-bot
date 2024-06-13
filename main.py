import asyncio

from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from config import dp, bot, session, stateStorage
from handlers.actions_list_handler import actionListRouter
from handlers.back_handler import backRouter
from handlers.balance_handler import balanceRouter
from handlers.general_purchases_analysis_handler import commonPurchasesAnalysisRouter
from handlers.info_handler import infoRouter
from handlers.login_handler import loginRouter, loginHandlerInit
from handlers.product_analysis_handler import productAnalysisRouter
from handlers.product_handler import productRouter
from middleware.auth_middleware import AuthorizationCheckMiddleware
from res.general_text import *
from state.app_state import AppState


@dp.message(Command(START_COMMAND))
async def startBot(message: Message, state: FSMContext) -> None:
    """
    Стартовая функция для запуска бота. Сразу переводит на шаг "Авторизация".
    :param message:
    :param state:
    :return: None
    """
    await message.answer(BOT_HELLO_MESSAGE, reply_markup=ReplyKeyboardRemove())
    await state.set_state(AppState.login)
    await loginHandlerInit(message=message, state=state)


if __name__ == "__main__":
    routerListForAuthRequired = [
        infoRouter,
        actionListRouter,
        commonPurchasesAnalysisRouter,
        balanceRouter,
        productRouter,
        productAnalysisRouter,
        backRouter,
    ]
    for router in routerListForAuthRequired:
        # Устанавливаем middleware для проверки авторизации к роутерам
        router.message.middleware(AuthorizationCheckMiddleware(
            session=session,
            storage=stateStorage
        ))

    dp.include_routers(
        loginRouter,
        *routerListForAuthRequired
    )
    asyncio.run(dp.start_polling(bot))
