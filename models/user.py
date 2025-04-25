from typing import Self
from sqlalchemy import text
from sqlalchemy.orm import Mapped, Session, mapped_column, relationship

from enums import RoleEnum
from models.profile import Profile
from settings.database import Base, connection, uniq_str_an


class User(Base):
    username: Mapped[uniq_str_an]
    password: Mapped[str]  # Mapped[bytes]
    email: Mapped[uniq_str_an]
    role: Mapped[RoleEnum] = mapped_column(
        default=RoleEnum.DEMO, server_default=text("'DEMO'")
    )

    profile: Mapped["Profile"] = relationship(
        "Profile",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan",
        lazy="joined",
    )

    @classmethod
    @connection
    def create(
        cls,
        username: str,
        password: str,
        email: str,
        session: Session = None,
        role: RoleEnum = RoleEnum.DEMO,
        **kwargs,
    ) -> Self:
        """_summary_

        Args:
            username (str): Имя пользователя
            password (str): Пароль пользователя(закодированный)
            email (str): Эл. почта пользователя
            session (Session, optional): Сессия. Defaults to None.
            role (RoleEnum, optional): Роль пользвателя . Defaults to RoleEnum.DEMO.
            **other_profile_data: Остальные данные для профила (см. Profile модель)
        Returns:
            Self: объект пользователя
        """

        new_user = cls(username=username, password=password, email=email, role=role)
        session.add(new_user)
        session.flush()
        
        new_profile = Profile(user_id=new_user.id, **kwargs.get('profile', {}))
        session.add(new_profile)
        session.commit()
        
        return new_user
