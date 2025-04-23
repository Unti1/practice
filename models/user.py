
from sqlalchemy import text
from sqlalchemy.orm import Mapped, Session, mapped_column, relationship
from enums import RoleEnum
from settings.database import Base, connection, uniq_str_an

class User(Base):
    username: Mapped[uniq_str_an]
    password: Mapped[str] # Mapped[bytes]
    email: Mapped[uniq_str_an]
    role: Mapped[RoleEnum] = mapped_column(default=RoleEnum.DEMO, server_default=text("'DEMO'"))
    
    profile: Mapped['Profile'] = relationship(
        "Profile",
        back_populates='user',
        uselist=False,
        cascade="all, delete-orphan",
        lazy="joined"
    )
            
    @classmethod
    @connection
    def create(cls, session: Session = None, **value):
        new_user = cls(**value)
        session.add(new_user)
        session.commit()
        
        
    