from telebot.types import Message
from config import bot


# Ветка диалога
def getName(message: Message):
    print(message.text)
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, getSurname)


def getSurname(message: Message):
    print(message.text)
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
