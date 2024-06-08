from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.fsm.storage.base import BaseStorage
from aiogram.types import TelegramObject
from sqlalchemy.orm import Session

from db.db import User
from res.login_text import PERMISSION_ERROR_TEXT
from state.general_state import AppState


class AuthorizationCheckMiddleware(BaseMiddleware):
    def __init__(self, session: Session, storage: BaseStorage):
        self.session: Session = session
        self.storage: BaseStorage = storage

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
            await event.answer(pe.__str__())
        except Exception as e:
            print(e)
            await event.answer(PERMISSION_ERROR_TEXT)
