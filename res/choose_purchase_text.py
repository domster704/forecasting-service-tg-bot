from res.general_actions_text import CREATE_PURCHASE_BUTTON_TEXT, CHOOSE_PURCHASE_BUTTON_TEXT
from res.general_text import BACK_BUTTON_TEXT

ACTIVE_PURCHASE_HELLO_TEXT = f"""🔎 Выбор закупки

Введите номер нужной закупки из списка, чтобы начать работать с ней.

↩️ Чтобы вернуться, нажмите кнопку <b>{BACK_BUTTON_TEXT}</b>."""

CHOOSE_PURCHASE_TEXT = lambda purchase: f"""🔎 Выбор закупки 
 
Вы выбрали закупку <b>{purchase}</b>. 
 
📚 По кнопке <b>{PRODUCT_INT_PURCHASE_BUTTON_TEXT}</b> вам доступна работа с товарами в закупке, включая:  
— прогноз потребности в товаре с учетом складских остатков; 
— детальную статистику по товару; 
— добавление товаров в закупку и ее редактирование. 
  
📥 По кнопке <b>{DOWNLOAD_PURCHASE_BUTTON_TEXT}</b> вы получите сформированный json-файл с информацией о закупке.  
 
🗑 Также вы можете <b>{DELETE_PURCHASE_BUTTON_TEXT}</b>. 
  
↩️ Чтобы вернуться, нажмите кнопку <b>{BACK_BUTTON_TEXT}</b>."""

PRODUCT_INT_PURCHASE_BUTTON_TEXT = "Товары"
DELETE_PURCHASE_BUTTON_TEXT = "Удалить закупку"
DOWNLOAD_PURCHASE_BUTTON_TEXT = "Скачать закупку"

DELETE_PURCHASE_SUCCESS_MESSAGE = "Закупка удалена"
NO_PURCHASES_TEXT = f"""В данный момент у вас нет закупок для выбора. 

📦 По кнопке <b>{CREATE_PURCHASE_BUTTON_TEXT}</b> вы сможете создать новую закупку и приступить к работе с ней.


❗️Следующее действие станет доступно только после создания закупки:
   
🔎 По кнопке <b>{CHOOSE_PURCHASE_BUTTON_TEXT}</b> вы сможете приступить к работе с уже созданными закупками."""
