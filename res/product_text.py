from res.general_text import BACK_BUTTON_TEXT

PRODUCT_HELLO_TEXT = f"Введите имя товара для его анализа и прогнозирования"

CALLBACK_DATA_PRODUCT_END = "product"
INPUT_WRONG_INDEX = "Вы ввели неправильный номер товара"

ANALYZE_PRODUCT_BUTTON_TEXT = "Аналитика по товару"
SUGGESTED_PRODUCT_BUTTON_TEXT = "Прогнозирование по товару"
PURCHASE_PRODUCT_BUTTON_TEXT = "Закупка товара"

PRODUCT_ACTIONS_TEXT = lambda product: f"""Выберите действие, которое вы хотите выполнить над товаром {product}:\n
- Кнопка <b>{ANALYZE_PRODUCT_BUTTON_TEXT}</b> позволит проанализировать товар.\n
- Кнопка <b>{SUGGESTED_PRODUCT_BUTTON_TEXT}</b> позволит посмотреть прогнозирования по товару.\n
- Кнопка <b>{PURCHASE_PRODUCT_BUTTON_TEXT}</b> позволит создать закупку товара.\n
- Кнопка <b>{BACK_BUTTON_TEXT}</b> поможет перейти на предыдущий этап.\n"""

SUGGESTED_PRODUCT_TEXT = "Какое-то прогнозирование с картинкой"

CHOSE_PERIOD_TEXT = "Выберите период"

YEAR_TEXT = "Год"
MONTH_TEXT = "Месяц"
QUARTER_TEXT = "Квартал"

SELECT_PERIOD_TEXT = lambda period: f"""Вы выбрали период {period}"""

CREATE_PURCHASE_INIT_MESSAGE_TEXT = ("Для создания закупки введите количество товара, субсчет, с баланса которого "
                                     "будет списываться сумма")
INPUT_PRODUCT_AMOUNT_TEXT = "Введите количество товара"
INPUT_SUB_ACCOUNT_TEXT = "Введите номер суб-субсчета"

PURCHASE_CREATE_SUCCESS_MESSAGE_TEXT = lambda purchase: f"Закупка {purchase} успешно создан"

CREATE_BUTTON_TEXT = "Создать"
EDIT_BUTTON_TEXT = "Редактировать"

WRONG_EDIT_PURCHASE_BECAUSE_NONE = ("Нет существующей закупки для данного товара. Для редактирования необходимо "
                                    "сначала создать закупку")

PURCHASE_EDIT_SUCCESS_MESSAGE_TEXT = lambda purchase: f"Закупка {purchase} сейчас будет изменена"
