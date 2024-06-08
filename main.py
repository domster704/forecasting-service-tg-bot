import asyncio

from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

from config import dp, bot, session
from res.general_text import *
from handlers.info import infoRouter
from handlers.login import loginRouter, CheckAuthorizationMiddleware


@dp.message(Command(START_COMMAND))
async def startBot(message: Message):
    markup = [
        [KeyboardButton(text=MESSAGE_REPLY_START)]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=markup,
                                   resize_keyboard=True,
                                   input_field_placeholder=START_COMMAND,
                                   one_time_keyboard=True)

    await message.answer(BOT_HELLO_MESSAGE, reply_markup=keyboard)


if __name__ == "__main__":
    infoRouter.message.middleware(CheckAuthorizationMiddleware(session=session))
    dp.include_routers(loginRouter, infoRouter)
    asyncio.run(dp.start_polling(bot))
