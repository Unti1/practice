
from decimal import Decimal
from enum import Enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from settings.database import Base

class OperationsEnum(str, Enum):
    INCOME = 'Заработано'
    OUTCOME = 'Потрачено'

class CurrencyEnum(str, Enum):
    USD = '$'
    RUR = '₽'

class UserBalance(Base):
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id'))
    amount: Mapped[Decimal]
    currency: Mapped[CurrencyEnum] = mapped_column(default=CurrencyEnum.RUR)
    type: Mapped[OperationsEnum]
    
    user: Mapped['User'] = relationship(
        'User',
        back_populates='userbalances'
    )