from datetime import datetime
from typing import Annotated, Self
from sqlalchemy import create_engine, func, select
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    class_mapper,
    declared_attr,
    mapped_column,
    query,
    sessionmaker,
)
from settings.config import settings

DATABASE_URL = settings.get_db_url()

engine = create_engine(DATABASE_URL)
session_maker = sessionmaker(engine, expire_on_commit=False)  # Фабрика сессий


uniq_str_an = Annotated[str, mapped_column(unique=True)]


def connection(method):
    def wrapper(*args, **kwargs):
        with session_maker() as session:
            try:
                return method(*args, session=session, **kwargs)
            except Exception as e:
                session.rollback()
                raise e
            finally:
                session.close()
    return wrapper


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    # id: Mapped[str] = mapped_column(primary_key=True, default=str(uuid.uuid4()))
    create_at: Mapped[datetime] = mapped_column(default=func.now())
    update_at: Mapped[datetime] = mapped_column(default=func.now(), onupdate=func.now())

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"
    
    @classmethod
    @connection
    def get(cls, session: Session = None, **creterias) -> None|Self:
        """Возвращает искомый объет базы данных по переданным creterias

        Args:
            session (Session, optional): Сессия запроса(подставляется автоматически). Defaults to None.
        Returns:
            None|Self: Объект или None
        """
        query = select(cls).filter_by(**creterias)
        rows = session.execute(query)
        return rows.scalar_one_or_none()
    
        
                
        
            
