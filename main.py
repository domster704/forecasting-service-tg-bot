import asyncio

from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from config import dp, bot, session, stateStorage
from handlers.actions_list_handler import actionListHandler
from handlers.back_handler import backRouter
from handlers.info import infoRouter
from handlers.login import loginRouter, loginHandlerInit
from middleware.auth_middleware import AuthorizationCheckMiddleware
from res.general_text import *
from state.general_state import AppState


@dp.message(Command(START_COMMAND))
async def startBot(message: Message, state: FSMContext) -> None:
    await message.answer(BOT_HELLO_MESSAGE, reply_markup=ReplyKeyboardRemove())
    await state.set_state(AppState.login)
    await loginHandlerInit(message=message, state=state)


if __name__ == "__main__":
    routerListForAuthRequired = [
        infoRouter,
        actionListHandler,
        backRouter
    ]
    for router in routerListForAuthRequired:
        router.message.middleware(AuthorizationCheckMiddleware(
            session=session,
            storage=stateStorage
        ))

    dp.include_routers(
        loginRouter,
        *routerListForAuthRequired
    )
    asyncio.run(dp.start_polling(bot))
