import asyncio

from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

from config import dp, bot, session, setAppState
from middleware.auth_middleware import AuthorizationCheckMiddleware
from res.general_text import *
from handlers.info import infoRouter
from handlers.login import loginRouter
from state.general_state import AppState


@dp.message(StateFilter(None), Command(START_COMMAND))
async def startBot(message: Message, state: FSMContext):
    await setAppState(state, AppState.start)

    markup = [
        [KeyboardButton(text=MESSAGE_REPLY_START)]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=markup,
                                   resize_keyboard=True,
                                   input_field_placeholder=START_COMMAND,
                                   one_time_keyboard=True)

    await message.answer(BOT_HELLO_MESSAGE, reply_markup=keyboard)
    await state.set_state(AppState.login)


if __name__ == "__main__":
    infoRouter.message.middleware(AuthorizationCheckMiddleware(session=session))
    dp.include_routers(loginRouter, infoRouter)
    asyncio.run(dp.start_polling(bot))
