

from sqlalchemy.orm import Mapped, Session
from settings.database import Base, connection


class User(Base):
    """Основная модель пользователя с полями
    id: int - Идентификатор пользователя
    username: str - Имя пользователя
    password: byte - Пароль пользоателя 
    email: str - Почта пользователя

    Args:
        Base (_type_): _description_
    """
    
    username : Mapped[str]
    password : Mapped[str]
    email : Mapped[str]
        
