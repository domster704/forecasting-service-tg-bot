from config import session
from db.db import User


async def logout(chat_id: int) -> bool:
    try:
        await session.delete(session.get(User, chat_id))
        await session.commit()
        return True
    except Exception as e:
        print(e)
        return False
