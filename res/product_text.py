from res.general_text import BACK_BUTTON_TEXT

CREATE_BUTTON_TEXT = "Ввести товар"
EDIT_BUTTON_TEXT = "Выбрать товар"

PRODUCT_ACTION_HELLO_TEXT = f"""📚 Товары

По кнопке <b>{CREATE_BUTTON_TEXT}</b> вы можете начать работать с новым товаром.

По кнопке <b>{EDIT_BUTTON_TEXT}</b> вы можете выбрать товар из уже добавленных в закупку ранее.

Выберите нужное действие, чтобы продолжить. 

↩️ Чтобы вернуться, нажмите кнопку <b>{BACK_BUTTON_TEXT}</b>."""

PRODUCT_HELLO_TEXT = f"""📚 <b>{CREATE_BUTTON_TEXT}</b>

Напишите название товара текстом.
 
↩️ Чтобы вернуться, нажмите кнопку <b>{BACK_BUTTON_TEXT}</b>."""

INPUT_PRODUCT_INDEX = "Введите номер товара из списка"
INPUT_WRONG_INDEX = "Вы ввели неправильный номер товара"

ANALYZE_PRODUCT_BUTTON_TEXT = "Аналитика по товару"
SUGGESTED_PRODUCT_BUTTON_TEXT = "Прогнозирование по товару"
PURCHASE_PRODUCT_BUTTON_TEXT = "Закупка товара"


def PRODUCT_ACTIONS_TEXT(product: str, regularity: bool):
    regularity_text = ""
    if regularity:
        regularity_text = "Регулярный"
    elif regularity == False:
        regularity_text = "Нерегулярный"
    elif regularity is None:
        regularity_text = "Регулярность неизвестна"

    return f"""Выберите действие, которое вы хотите выполнить над товаром {product} <b>({regularity_text})</b>. 
 
📊 Кнопка <b>{ANALYZE_PRODUCT_BUTTON_TEXT}</b> позволит узнать складские остатки товара, полную информацию по 
последним закупкам товара в формате Excel, статистику закупок товара по цене и количеству за разные временные периоды 
и аналитику по обороту дебет/кредит.

🧾 По кнопке <b>{PURCHASE_PRODUCT_BUTTON_TEXT}</b> вы добавите товар в выбранную вами закупку.

📈 По кнопке <b>{SUGGESTED_PRODUCT_BUTTON_TEXT}</b> вам доступен прогноз потребности в товаре на будущий период. 
Прогноз доступен только для регулярных закупок.

<i>Узнать (не)регулярность закупки вы можете в скобках рядом с названием товара в этом сообщении. Критерии, по которым 
определяется регулярность закупки товара: 1. Товар закупался более 3 раз 2. Товар закупался в разные временные периоды</i>

 ↩️ Чтобы вернуться, нажмите кнопку <b>{BACK_BUTTON_TEXT}</b>."""


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

WRONG_EDIT_PURCHASE_BECAUSE_NONE = ("Нет существующей закупки для данного товара. Для редактирования необходимо "
                                    "сначала создать закупку")

NO_PRODUCTS_IN_PURCHASE_TEXT = f"""📚 Товары 
 
Похоже, что вы еще не добавили ни одного товара в закупку.

Начните работу с новым товаром по кнопке <b>{CREATE_BUTTON_TEXT}</b>. 
 
↩️ Чтобы вернуться, нажмите кнопку <b>{BACK_BUTTON_TEXT}</b>."""

ADDING_SUCCESS = "Товар успешно добавлен"

YOU_CHOOSE_THAT_PRODUCT_TEXT = lambda product_name: f"Вы выбрали <b>{product_name}</b>"
