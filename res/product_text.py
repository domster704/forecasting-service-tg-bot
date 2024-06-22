from res.general_text import BACK_BUTTON_TEXT

PRODUCT_ACTION_HELLO_TEXT = f"""Выберите нужное действие"""

PRODUCT_HELLO_TEXT = f"""🔎 <b>Введите название товара</b>

Напишите название товара текстом.

↩️ Чтобы вернуться, нажмите кнопку <b>{BACK_BUTTON_TEXT}</b>."""

INPUT_PRODUCT_INDEX = "Введите номер товара из списка"
INPUT_WRONG_INDEX = "Вы ввели неправильный номер товара"

ANALYZE_PRODUCT_BUTTON_TEXT = "Аналитика по товару"
SUGGESTED_PRODUCT_BUTTON_TEXT = "Прогнозирование по товару"
PURCHASE_PRODUCT_BUTTON_TEXT = "Закупка товара"

PRODUCT_ACTIONS_TEXT = lambda product, regular: \
    f"""Выберите действие, которое вы хотите выполнить над товаром 
    {product} (<b>{"Регулярный" if regular else ("Нерегулярный" if not regular else "Регулярность неизвестна")}</b>):\n
- Кнопка <b>{ANALYZE_PRODUCT_BUTTON_TEXT}</b> позволит проанализировать товар.\n
- Кнопка <b>{SUGGESTED_PRODUCT_BUTTON_TEXT}</b> позволит посмотреть прогнозирования по товару.\n
- Кнопка <b>{PURCHASE_PRODUCT_BUTTON_TEXT}</b> позволит создать закупку товара.\n
- Кнопка <b>{BACK_BUTTON_TEXT}</b> поможет перейти на предыдущий этап.\n

Критерий регулярности:
1. Товар закупался больше 3 раз
2. Товар закупался в разные периоды"""

SUGGESTED_PRODUCT_TEXT = "Какое-то прогнозирование с картинкой"

CREATE_PURCHASE_INIT_MESSAGE_TEXT = f"""Для создания закупки товара введите 6 сообщений в соответствии со списком:
1. Объем поставки
2. Сумма спецификации
3. Дата начала поставки
4. Дата окончания поставки
5. Условия поставки
"""
INPUT_PRODUCT_AMOUNT_TEXT = "Введите количество товара"
INPUT_SUB_ACCOUNT_TEXT = "Введите номер суб-субсчета"

CREATE_BUTTON_TEXT = "Ввести товар"
EDIT_BUTTON_TEXT = "Выбрать товар"

WRONG_EDIT_PURCHASE_BECAUSE_NONE = ("Нет существующей закупки для данного товара. Для редактирования необходимо "
                                    "сначала создать закупку")

NO_PRODUCTS_IN_PURCHASE_TEXT = "Нет товаров в закупке"
ADDING_SUCCESS = "Товар успешно добавлен"
