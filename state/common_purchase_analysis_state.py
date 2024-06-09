from aiogram.fsm.state import StatesGroup, State


class CommonPurchaseAnalysisState(StatesGroup):
    waitPressButtons = State()
    purchaseStatistics = State()
    expensivePurchase = State()
