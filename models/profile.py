

from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from settings.database import Base


class Profile(Base):
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id'))
    phone: Mapped[str|None]
    name: Mapped[str|None]
    suname: Mapped[str|None]
    about: Mapped[str|None]
    date_birthday: Mapped[datetime|None]
    
    user: Mapped['User'] = relationship(
        "User",
        back_populates='profile',
        uselist=False
    )