from datetime import datetime
from typing import Annotated
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
    def get(cls, session: Session = None, **creterias):
        query = select(cls).filter_by(**creterias)
        rows = session.execute(query)
        return rows.scalar_one_or_none()
     
    @classmethod
    @connection
    def get_all_by_creterias(cls, session: Session = None, **creterias):
        query = select(cls).filter_by(**creterias)
        rows = session.execute(query)
        return rows.scalars().all()
    
    @classmethod
    @connection
    def get_all(cls, session: Session = None):
        query = select(cls)
        rows = session.execute(query)
        return rows.scalars().all()
    
    @classmethod
    @connection
    def create(
        cls,
        session: Session = None,
        **data,
    ):
        new_row = cls(**data)
        session.add(new_row)
        session.commit()
        return new_row

    @classmethod
    @connection
    def create_many(
        cls,
        datas: list[dict],
        session: Session = None,
    ):
        new_rows = [cls(**data) for data in datas]
        session.add_all(new_rows)
        session.commit()
        return new_rows

    @classmethod
    @connection
    def update(
        cls,
        id: int,
        session: Session = None,
        **data
    ):
        query = select(cls).where(cls.id == id).with_for_update()
        rows = session.execute(query)
        concrete_row = rows.scalar_one_or_none()

        
        if not concrete_row:
            raise ValueError(f'Данные с таким id в таблице {cls.__tablename__} не найдены')
        
        for key, value in data.items():
            if key not in concrete_row.__dict__:
                raise ValueError(f'Колонки "{key}" нету в таблице {cls.__tablename__}')
            if getattr(concrete_row, key) != value:
                setattr(concrete_row, key, value)
        
        session.commit()
        return concrete_row
    
    @classmethod
    @connection
    def delete(
        cls,
        id: int,
        session: Session = None,
    ): 
        query = select(cls).where(cls.id == id)
        rows = session.execute(query)
        row = rows.scalar_one_or_none()
        if row:
            session.delete(row)
            session.commit()
            return True
        return False
    
    def to_dict(self) -> dict:
        columns = class_mapper(self.__class__).columns
        return {column.key: getattr(self, column.key) for column in columns}
    
        
                
        
            
