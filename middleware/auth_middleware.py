from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import TelegramObject, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy.orm import Session

from db.db import User
from res.login_text import *
from state.general_state import AppState


class AuthorizationCheckMiddleware(BaseMiddleware):
    def __init__(self, session: Session, storage: MemoryStorage):
        self.session: Session = session
        self.storage: MemoryStorage = storage

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        try:
            if await self.session.get(User, event.chat.id) is None:
                raise PermissionError(PERMISSION_ERROR_TEXT)

            return await handler(event, data)
        except PermissionError as pe:
            await self.storage.set_state(AppState.login)

            builder = InlineKeyboardBuilder()
            builder.add(InlineKeyboardButton(
                text=DO_AUTHORIZATION,
                callback_data=TRY_AGAIN_ACTION
            ))

            await event.answer(pe.__str__(), reply_markup=builder.as_markup())
        except Exception as e:
            print(e)
            await event.answer(PERMISSION_ERROR_TEXT)
