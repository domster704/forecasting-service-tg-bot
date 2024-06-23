from aiogram.fsm.state import StatesGroup, State


class AddProductToPurchase(StatesGroup):
    """
    Класс для описания состояний в разделе <Добавление товара в закупку>
    """

    purchaseAmount = State()  # Состояние ввода объема поставки
    nmc = State()  # Состояние ввода суммы спецификации (цена товара)
    dateStart = State()  # Состояние ввода даты начала поставки
    dateEnd = State()  # Состояние ввода даты окончания поставки
    deliveryConditions = State()  # Состояние ввода условий поставки
    entityId = State()  # Состояние ввода сквозного идентификатора СПГЗ (название товара)
