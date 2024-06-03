import json

from telebot import TeleBot, types

env: dict = json.load(open("env.json"))

bot = TeleBot(env["apiTG"])

MESSAGE_REPLY_START = "Начать"
CALLBACK_DATA_HANDLER_MESSAGE = "yes"


@bot.message_handler(commands=['start'])
def startBot(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(MESSAGE_REPLY_START)
    btn2 = types.KeyboardButton("Задать вопрос")
    btn3 = types.KeyboardButton("Test")
    markup.add(btn1).row(btn2, btn3)

    bot.send_message(message.chat.id, 'Я ассистент по закупкам', parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(message, getName)  # следующий шаг – функция get_name


# Ветка диалога
def getName(message):
    print(message.text)
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, getSurname)


def getSurname(message):
    print(message.text)
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')


@bot.message_handler(content_types=['text'])
def getText(message):
    if message.text and message.text == MESSAGE_REPLY_START:
        first_mess = (f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет, я бот для "
                      f"прогнозирования закупок")
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text='Да', callback_data=CALLBACK_DATA_HANDLER_MESSAGE))
        bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def response(function_call):
    if function_call.message and function_call.data == CALLBACK_DATA_HANDLER_MESSAGE:
        second_mess = "test"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://google.com"))
        bot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        bot.answer_callback_query(function_call.id)


bot.infinity_polling()
