
from sqlalchemy.orm import Session
from sqlalchemy import select
import config
from sqlalchemy import create_engine
from models.base import Base
from models.user import User
from models.address import Address
engine = create_engine(
    url = config.SQLALCHEMY_URL,
    echo = config.SQLALCHEMY_ECHO,
)

#Контекстынй менеджер для работы с сессией БД    
with Session(engine) as session:
    #добавление данных в базу, согласно нашим моделям orm
    # spongebob = User(
    #     name="spongebob",
    #     fullname="Spognebob Squarepants",
    #     addresses=[Address(email_address="spongebob@sqlalchemy.org")],
    # )
    # sandy = User(
    #     name="sandy",
    #     fullname="Sandy Cheeks",
    #     addresses=[
    #         Address(email_address="sandy@sqlalchemy.org"),
    #         Address(email_address="sandy@squirrelpower.org"),
    #     ],
    # )
    # patrick = User(
    #     name="patrick",
    #     fullname="Patrick Star",
    # )
    # #Добавляем наши данные в базу
    # session.add_all([spongebob, sandy, patrick])
    # #Сохраняем изменения и закрываем сессию
    # session.commit()
    
    
    #выборка данных с помощью оператора select
    # session = Session(engine)
    # stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))
    # for user in session.scalars(stmt):
    #     print(user)
    #запрос select + join
    stmt = (
        select(Address)
        .join(Address.user)
        .where(User.name == "sandy")
        .where(Address.email_address == "sandy@sqlalchemy.org")

    )
    
Base.metadata.create_all(engine)    
        