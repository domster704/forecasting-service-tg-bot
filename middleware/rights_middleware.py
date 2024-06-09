from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.dispatcher.flags import get_flag
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import TelegramObject, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy.orm import Session

from db.db import User
from res.login_text import *
from state.general_state import AppState


class RightsCheckMiddleware(BaseMiddleware):
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
            rights = get_flag(data, "rights")
            print(rights)
            if False:
                raise PermissionError(PERMISSION_RIGHTS_ERROR_TEXT)

            return await handler(event, data)
        except PermissionError as pe:
            print(pe)
        except Exception as e:
            print(e)
            await event.answer(PERMISSION_RIGHTS_ERROR_TEXT)
