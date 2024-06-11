from __future__ import annotations

from typing import Union

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Pagination(object):
    CALLBACK_DATA_START_NEXT = "next_page_"
    CALLBACK_DATA_START_PREV = "prev_page_"

    """
    Класс для генерации постраничного меню
    """

    def __init__(
            self,
            items: list,
            max_items_per_page: int = 5,
            callback_data_end: str = ""
    ):
        """
        :param items:
        :param max_items_per_page:
        :param callback_data_end: Строчка, которая будет конкатенирована в
        конце callback_data у inline-кнопок. То есть для кнопки `Вперед` и `Назад
        будет {self.CALLBACK_DATA_START_NEXT}{self.callback_data_end} и
        {self.CALLBACK_DATA_START_PREV}{self.callback_data_end} соответственно callback_data.
        По умолчанию будет callback_data_end - пустая строка.
        """
        self.items: list = items
        self.__max_items_per_page: int = max_items_per_page
        self.__current_page: int = 0
        self.callback_data_end: str = callback_data_end
        self.keyboard: Union[InlineKeyboardMarkup] = self.__generateKeyboard()

        self.__start = self.__max_items_per_page * self.__current_page
        self.__end = self.__max_items_per_page * (self.__current_page + 1)

    def __recalcStartAndEnd(self) -> None:
        self.__start = self.__max_items_per_page * self.__current_page
        self.__end = self.__max_items_per_page * (self.__current_page + 1)

    def __generateKeyboard(self) -> Union[InlineKeyboardMarkup]:
        keyboardList = [
            InlineKeyboardButton(
                text="Назад",
                callback_data=f"{self.CALLBACK_DATA_START_PREV}{self.callback_data_end}"
            ) if self.__current_page != 0 else None,
            InlineKeyboardButton(
                text="Вперед",
                callback_data=f"{self.CALLBACK_DATA_START_NEXT}{self.callback_data_end}"
            ) if (self.__current_page + 1) * self.__max_items_per_page <= len(self.items) else None,
        ]

        keyboard = InlineKeyboardBuilder().row(
            *filter(lambda elem: elem is not None, keyboardList)
        )

        return keyboard.as_markup()

    def nextPage(self) -> Pagination:
        if (self.__current_page + 1) * self.__max_items_per_page <= len(self.items):
            self.__current_page += 1

        self.keyboard: Union[InlineKeyboardMarkup] = self.__generateKeyboard()
        self.__recalcStartAndEnd()
        return self

    def prevPage(self) -> Pagination:
        if self.__current_page != 0:
            self.__current_page -= 1

        self.keyboard: Union[InlineKeyboardMarkup] = self.__generateKeyboard()
        self.__recalcStartAndEnd()
        return self

    def __getMessageText(self) -> str:
        return "\n".join([
            f"{self.__current_page * self.__max_items_per_page + i + 1}. {item}" for i, item in
            enumerate(self.items[self.__start:self.__end])
        ])

    def getMessageData(self) -> dict[str, InlineKeyboardMarkup | str]:
        return {"text": self.__getMessageText(), "reply_markup": self.keyboard}
