from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from res.info_text import *

infoRouter = Router()


async def infoHandlerInit(message: Message):
    keyboard = ReplyKeyboardBuilder().add(
        KeyboardButton(text=HELP_BUTTON_TEXT)
    ).row(
        KeyboardButton(text=USER_INFO_BUTTON_TEXT),
        KeyboardButton(text=CONTINUE_BUTTON_TEXT)
    )

    await message.answer(text=INFO_TEXT, reply_markup=keyboard.as_markup(resize_keyboard=True))

# @bot.message_handler(func=lambda message: message.text == HELP_BUTTON_TEXT)
# def get_help(message, error):
#     if type(error) is PermissionError:
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         retry_button = types.KeyboardButton(text=TRY_AUTH_MESSAGE)
#         markup.add(retry_button)
#
#         bot.send_message(message.chat.id, PERMISSION_ERROR_TEXT, parse_mode='html', reply_markup=markup)
#         return
#
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     retry_button = types.KeyboardButton(text=BACK_BUTTON_TEXT)
#     markup.add(retry_button)
#     bot.send_message(message.chat.id, PERMISSION_ERROR_TEXT, parse_mode='html', reply_markup=markup)
#
#
# @bot.message_handler(func=lambda message: message.text == BACK_BUTTON_TEXT)
# @isAuth
# def get_help(message, error):
#     if type(error) is PermissionError:
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         retry_button = types.KeyboardButton(text=TRY_AUTH_MESSAGE)
#         markup.add(retry_button)
#
#         bot.send_message(message.chat.id, PERMISSION_ERROR_TEXT, parse_mode='html', reply_markup=markup)
#         return
