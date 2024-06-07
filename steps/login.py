from telebot import types
from telebot.types import Message

from config import bot
from res.login_text import *
from steps.info import InfoStep
from viewModel import vm


class AuthorizationStep(object):
    def __init__(self):
        self.authDataChecker: AuthorizationDataChecker = AuthorizationDataChecker()
        self.rights = []

    def init(self, message: Message):
        bot.send_message(message.chat.id, REQUIRE_AUTHORIZED)
        self.getLogin(message)

    def getLogin(self, message: Message):
        bot.send_message(message.chat.id, ENTER_LOGIN)
        bot.register_next_step_handler(message, self.getPassword)

    def getPassword(self, message: Message):
        # Получаем логин из предыдущего сообщения
        self.authDataChecker.setLogin(message.text)

        bot.send_message(message.chat.id, ENTER_PASSWORD)
        bot.register_next_step_handler(message, self.checkLoginAndPassword)

    def checkLoginAndPassword(self, message: Message):
        # Получаем пароль из предыдущего сообщения
        self.authDataChecker.setPassword(message.text)

        self.authDataChecker.checkData()
        if not self.authDataChecker.isAuth:
            markup = types.InlineKeyboardMarkup()
            retry_button = types.InlineKeyboardButton(text=TRY_AGAIN_ACTION, callback_data=TRY_AGAIN_ACTION)
            markup.add(retry_button)

            bot.send_message(message.chat.id, WRONG_LOGIN_OR_PASSWORD, parse_mode='html', reply_markup=markup)
            return

        bot.send_message(message.chat.id, RIGHT_LOGIN_AND_PASSWORD)
        vm.infoStep = InfoStep()

        vm.infoStep.init(message)


class AuthorizationDataChecker(object):
    def __init__(self):
        self.__login: str = ""
        self.__password: str = ""
        self.isAuth: bool = False

    def setLogin(self, login: str) -> None:
        self.__login = login

    def setPassword(self, password: str) -> None:
        self.__password = password

    def __checkLogin(self) -> bool:
        return self.__login == "test123"

    def __checkPassword(self) -> bool:
        return self.__password == "test123"

    def checkData(self) -> None:
        self.isAuth = self.__checkLogin() and self.__checkPassword()


@bot.callback_query_handler(func=lambda call: call.data == TRY_AGAIN_ACTION)
def retry_login(call: types.CallbackQuery):
    if not hasattr(vm, 'auth'):
        return

    message = bot.send_message(call.message.chat.id, TRY_AGAIN_MESSAGE)
    vm.auth.getLogin(message)
    bot.answer_callback_query(call.id)
