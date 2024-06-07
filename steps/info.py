from telebot import types
from telebot.types import Message

from config import bot
from decorators import isAuth
from res.info_text import *


class InfoStep(object):
    def __init__(self):
        pass

    @isAuth
    def init(self, message: Message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        help_button = types.KeyboardButton(HELP_BUTTON_TEXT)
        user_info_button = types.KeyboardButton(USER_INFO_BUTTON_TEXT)
        continue_button = types.KeyboardButton(CONTINUE_BUTTON_TEXT)

        markup.add(continue_button).row(help_button, user_info_button)

        bot.send_message(message.chat.id, text=INFO_TEXT, parse_mode="html", reply_markup=markup)

    @isAuth
    def get_help(self, message: Message):
        bot.send_message()
