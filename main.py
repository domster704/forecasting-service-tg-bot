from config import bot
from telebot import types
from telebot.types import Message, CallbackQuery
from branches.user_info import getName
from res.text import *


@bot.message_handler(commands=['start'])
def startBot(message: Message):
    print(type(message))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(MESSAGE_REPLY_START)
    btn2 = types.KeyboardButton(ASK_QUESTION_MESSAGE)
    btn3 = types.KeyboardButton("Test")
    markup.add(btn1).row(btn2, btn3)

    bot.send_message(message.chat.id, BOT_HELLO_MESSAGE, parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(message, getName)  # следующий шаг – функция get_name


@bot.message_handler(content_types=['text'])
def getText(message: Message):
    if message.text and message.text == MESSAGE_REPLY_START:
        first_mess = FIRST_MESSAGE(message)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text='Да', callback_data=CALLBACK_DATA_HANDLER_MESSAGE))
        bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def response(function_call: CallbackQuery):
    print(type(function_call))
    if function_call.message and function_call.data == CALLBACK_DATA_HANDLER_MESSAGE:
        second_mess = "test"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://google.com"))
        bot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        bot.answer_callback_query(function_call.id)


bot.infinity_polling()
