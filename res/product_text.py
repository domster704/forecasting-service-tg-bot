from res.general_text import *

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
определяется регулярность закупки товара: 
1. Товар закупался более 3 раз 
2. Товар закупался в разные временные периоды</i>

 ↩️ Чтобы вернуться, нажмите кнопку <b>{BACK_BUTTON_TEXT}</b>."""


def CREATE_PURCHASE_INIT_MESSAGE_TEXT(amount, nmc, date_start, date_end):
    return f"""1. Объем поставки (<b>{amount}</b>)
2. Сумма спецификации (<b>{nmc}</b> {"рублей" if nmc is not None and len(str(nmc)) != 0 else ""})
3. Дата начала поставки (<b>{date_start}</b>) 
4. Дата окончания поставки (<b>{date_end}</b>) 
5. Условия поставки ()

↩️ Чтобы вернуться, нажмите кнопку <b>{BACK_BUTTON_TEXT}</b>. """


ADD_PRODUCT_TO_PURCHASE_MESSAGE_TEXT = f"""🧾 <b>Закупка товара </b>
 
Чтобы создать закупку товара, выберите пункты из меню ниже, которые вы хотите заполнить. В скобках указаны значения, 
которые будут выставлены по умолчанию, если вы решите не заполнять пункт."""

ADD_PRODUCT_AMOUNT_BUTTON = "Объем поставки"
ADD_PRODUCT_PRICE_BUTTON = "Сумма спецификации"
ADD_PRODUCT_DATE_START_BUTTON = "Дата начала поставки"
ADD_PRODUCT_DATE_END_BUTTON = "Дата окончания поставки"
ADD_PRODUCT_DELIVERY_BUTTON = "Условия поставки"

SETTING_VALUE = "Значение сохранено"

FINISH_ADDING_PRODUCT = "Завершить закупку товара"

EDIT_PRODUCT_BUTTON_TEXT = "Редактировать"
CREATE_PRODUCT_BUTTON_TEXT = "Создать"


def SELECT_PERIOD_TEXT(period):
    return f"""📈 <b>Прогнозирование по товару</b> 
 
Вы выбрали прогноз на <b>{period}</b>. Выберите, какой тип прогноза вы хотите получить. Вам доступны прогнозы <b>по 
количеству</b> и <b>по цене</b> закупки.
 
↩️ Чтобы вернуться, нажмите кнопку <b>{BACK_BUTTON_TEXT}</b>."""


NO_PRODUCTS_IN_PURCHASE_TEXT = f"""📚 <b>Товары</b>
 
Похоже, что вы еще не добавили ни одного товара в закупку.

Начните работу с новым товаром по кнопке <b>{CREATE_BUTTON_TEXT}</b>. 
 
↩️ Чтобы вернуться, нажмите кнопку <b>{BACK_BUTTON_TEXT}</b>."""

ADDING_SUCCESS = f"""🧾 Закупка товара 
 
Товар успешно добавлен в закупку."""

YOU_CHOOSE_THAT_PRODUCT_TEXT = lambda product_name: f"Вы выбрали <b>{product_name}</b>"

PREDICT_PRODUCT_PERIOD_TEXT = f"""📈 Прогнозирование по товару

Выберите период, прогноз потребности на который хотите увидеть. Вам доступен прогноз на месяц, квартал и год.

↩️ Чтобы вернуться, нажмите кнопку <b>{BACK_BUTTON_TEXT}</b>."""
