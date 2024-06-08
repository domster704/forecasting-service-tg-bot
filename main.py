from aiogram.filters import Command
from telebot import types
from telebot.types import Message

from config import bot, dp
from res.general_text import *
from res.login_text import *
from state.auth_state import AuthState
from steps.login import AuthorizationStep


@dp.message(Command(START_COMMAND))
def startBot(message: Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = types.KeyboardButton(MESSAGE_REPLY_START)
    markup.add(start_button)

    bot.set_state(message.from_user.id, AuthState.auth, message.chat.id)
    bot.send_message(message.chat.id, BOT_HELLO_MESSAGE, parse_mode='html', reply_markup=markup)
    auth = AuthorizationStep()
    bot.register_next_step_handler(message, auth.init)


@bot.message_handler(content_types=['text'])
def getText(message: Message):
    if message.text and message.text == TRY_AUTH_MESSAGE:
        vm.auth = AuthorizationStep()
        vm.auth.init(message)


#
#
# @bot.callback_query_handler(func=lambda call: True)
# def response(function_call: CallbackQuery):
#     if function_call.message and function_call.data == CALLBACK_DATA_HANDLER_MESSAGE:
#         second_mess = "test"
#         markup = types.InlineKeyboardMarkup()
#         markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://google.com"))
#         bot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
#         bot.answer_callback_query(function_call.id)


bot.infinity_polling()
