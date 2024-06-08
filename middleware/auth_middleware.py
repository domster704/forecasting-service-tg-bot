from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.orm import Session

from db.db import User
from res.login_text import PERMISSION_ERROR_TEXT


class AuthorizationCheckMiddleware(BaseMiddleware):
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
