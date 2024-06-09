from config import session
from db.db import User


async def logout(chat_id: int) -> bool:
    """

    :param chat_id: - идентификатор чата для получения объекта пользователя из БД
    :return: bool - успешный выход из аккаунта или нет
    """
    try:
        await session.delete(await session.get(User, chat_id))
        await session.commit()
        return True
    except Exception as e:
        print(e)
        return False
