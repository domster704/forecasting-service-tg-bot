from telebot import types
from telebot.types import Message, CallbackQuery

from res.general_text import MESSAGE_REPLY_START
from steps.login import AuthorizationStep
from config import bot
from res.login_text import *
from viewModel import vm


@bot.message_handler(commands=['start'])
def startBot(message: Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = types.KeyboardButton(MESSAGE_REPLY_START)
    markup.add(start_button)

    bot.send_message(message.chat.id, BOT_HELLO_MESSAGE, parse_mode='html', reply_markup=markup)
    vm.auth = AuthorizationStep()
    bot.register_next_step_handler(message, vm.auth.init)


# @bot.message_handler(content_types=['text'])
# def getText(message: Message):
#     if message.text and message.text == MESSAGE_REPLY_START:
#         first_mess = FIRST_MESSAGE(message)
#         markup = types.InlineKeyboardMarkup()
#         markup.add(types.InlineKeyboardButton(text='Да', callback_data=CALLBACK_DATA_HANDLER_MESSAGE))
#         bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)
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
