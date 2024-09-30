from sqlalchemy.orm import DeclarativeBase

#Базовый класс от которого наследуются остальные пользовательские классы 
class Base(DeclarativeBase):
    pass