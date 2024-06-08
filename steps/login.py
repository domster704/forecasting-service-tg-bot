from typing import Callable, Dict, Any, Awaitable

from aiogram import types, Router, F, BaseMiddleware
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import TelegramObject
from sqlalchemy.orm import Session

from config import session
from db.db import User
from res.general_text import MESSAGE_REPLY_START, SOMETHING_WRONG
from res.login_text import *
from state.auth_state import AuthState

loginRouter = Router()


@loginRouter.message(StateFilter(None), F.text == MESSAGE_REPLY_START)
async def init(message: types.Message, state: FSMContext):
    await message.answer(REQUIRE_AUTHORIZED)
    await message.answer(ENTER_LOGIN)
    await state.set_state(AuthState.login)


@loginRouter.message(AuthState.login)
async def getLogin(message: types.Message, state: FSMContext):
    await state.update_data(login=message.text.lower())
    await message.answer(ENTER_PASSWORD)
    await state.set_state(AuthState.password)


@loginRouter.message(AuthState.password)
async def getPassword(message: types.Message, state: FSMContext):
    await state.update_data(password=message.text.lower())
    auth: AuthorizationDataChecker = AuthorizationDataChecker(**await state.get_data())
    try:
        await state.set_state({})
        await session.add(User(id=message.from_user.id, isAuth=auth.isAuth))

        if auth.isAuth:
            await message.answer(RIGHT_LOGIN_AND_PASSWORD)
            return

        await message.answer(WRONG_LOGIN_OR_PASSWORD)
    except Exception as e:
        await message.answer(SOMETHING_WRONG)


class AuthorizationDataChecker(object):
    def __init__(self, login: str, password: str):
        self.__login: str = login
        self.__password: str = password
        self.isAuth: bool = self.__checkData()

    def __checkLogin(self) -> bool:
        return self.__login == "test123"

    def __checkPassword(self) -> bool:
        return self.__password == "test123"

    def __checkData(self) -> bool:
        return self.__checkLogin() and self.__checkPassword()

    def __str__(self) -> str:
        return f"Login: {self.__login}, Password: {self.__password}"


# @bot.callback_query_handler(func=lambda call: call.data == TRY_AGAIN_ACTION)
# def retry_login(call: types.CallbackQuery):
#     if not hasattr(vm, 'auth'):
#         return
#
#     message = bot.send_message(call.message.chat.id, TRY_AGAIN_MESSAGE)
#     vm.auth.getLogin(message)
#     bot.answer_callback_query(call.id)

class CheckAuthorizationMiddleware(BaseMiddleware):
    def __init__(self, session: Session):
        self.session: Session = session

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        try:
            if await self.session.get(User, event.chat.id) is None:
                await event.answer(PERMISSION_ERROR_TEXT)
                return

            return await handler(event, data)
        except Exception as e:
            print(e)
            await event.answer(PERMISSION_ERROR_TEXT)
