from typing import Callable, Dict, Any, Awaitable

from aiogram import types, Router, F, BaseMiddleware
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import TelegramObject, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy.orm import Session

from config import session
from db.db import User
from handlers.info import infoHandlerInit
from res.general_text import MESSAGE_REPLY_START, SOMETHING_WRONG
from res.login_text import *
from state.auth_state import AuthState

loginRouter = Router()


@loginRouter.message(StateFilter(None), F.text == MESSAGE_REPLY_START)
async def loginHandlerInit(message: types.Message, state: FSMContext):
    user_login_info: User = await session.get(User, message.from_user.id)
    if user_login_info is not None and user_login_info.isAuth:
        await goToInfoHandler(message)
        return

    await message.answer(REQUIRE_AUTHORIZED)
    await message.answer(ENTER_LOGIN)
    await state.set_state(AuthState.login)


@loginRouter.callback_query(StateFilter(None), F.data == TRY_AGAIN_ACTION)
async def loginHandlerCallbackInit(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(ENTER_LOGIN)
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
        await state.clear()

        if auth.isAuth:
            session.add(User(id=message.from_user.id, isAuth=auth.isAuth))
            await session.commit()

            await message.answer(RIGHT_LOGIN_AND_PASSWORD)
            await goToInfoHandler(message)
            return

        raise PermissionError(WRONG_LOGIN_OR_PASSWORD)
    except PermissionError as pe:
        builder = InlineKeyboardBuilder()
        builder.add(InlineKeyboardButton(
            text=TRY_AGAIN_ACTION,
            callback_data=TRY_AGAIN_ACTION
        ))

        await message.answer(pe.__str__(), reply_markup=builder.as_markup())
    except Exception as e:
        print(e)
        await message.answer(SOMETHING_WRONG)


async def goToInfoHandler(message: types.Message):
    print("auth")
    await infoHandlerInit(message)


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
