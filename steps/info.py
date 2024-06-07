from telebot import types
from telebot.types import Message

from config import bot
from decorators import isAuth
from res.general_text import MESSAGE_REPLY_START
from res.info_text import *
from res.login_text import TRY_AUTH_MESSAGE


class InfoStep(object):
    def __init__(self):
        pass

    @isAuth
    def init(self, message: Message, error):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        help_button = types.KeyboardButton(HELP_BUTTON_TEXT)
        user_info_button = types.KeyboardButton(USER_INFO_BUTTON_TEXT)
        continue_button = types.KeyboardButton(CONTINUE_BUTTON_TEXT)

        markup.add(continue_button).row(help_button, user_info_button)

        bot.send_message(message.chat.id, text=INFO_TEXT, parse_mode="html", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == HELP_BUTTON_TEXT)
@isAuth
def get_help(message, error):
    if type(error) is PermissionError:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        retry_button = types.KeyboardButton(text=f"{TRY_AUTH_MESSAGE}")
        markup.add(retry_button)

        bot.send_message(message.chat.id, PERMISSION_ERROR_TEXT, parse_mode='html', reply_markup=markup)
        return

    print(123)
