from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base
#Если импортировать просто .user import USer получится циклический импорт, модули будут импортировать друг друга
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .user import User

#Пользовательский класс address    
class Address(Base):
    #имя таблицы
    __tablename__ = "address"
    #столбцы для таблицы в БД
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    
    #relationship связывает 2 класса орм юзера и адрес
    #Address.user сввязывает address с user
    user: Mapped["User"] = relationship(back_populates="addresses")
        
    
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"