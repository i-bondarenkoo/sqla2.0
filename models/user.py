from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from .base import Base


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .address import Address
#Пользовательский класс user
class User(Base):
    #имя таблицы
    __tablename__ = "user_account"
    #столбцы для таблицы в БД
    #за счет mapped осуществляется аннотация типов
    #более конкретная информация указывается далее с помощью mapped_column
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[str | None]
    #relationship связывает 2 класса орм юзера и адрес
    #User.address связывает user с address
    addresses: Mapped[list["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"