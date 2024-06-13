from aiogram.fsm.state import StatesGroup, State


class ProductState(StatesGroup):
    """
    Класс для описания состояний в разделе <Товар>
    """
    productName = State()
    productNameSuggestedList = State()
    enterProductNumFromList = State()

    productActions = State()
    productWaitActions = State()
    productAnalysis = State()
    productSuggestion = State()
    productPurchase = State()

    choosePeriod = State()
