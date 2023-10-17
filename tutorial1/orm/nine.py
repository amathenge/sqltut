from datetime import datetime
from typing import Optional
from sqlalchemy import func, create_engine, insert, text, select, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, MappedAsDataclass, sessionmaker

class Base(MappedAsDataclass, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'user_account'
    __table_args__ = {'sqlite_autoincrement': True}
    id: Mapped[int] = mapped_column(primary_key=True, init=False, autoincrement=True)
    name: Mapped[str]
    fullname: Mapped[Optional[str]]
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())

class Address(Base):
    __tablename__ = 'address'
    __table_args__ = {'sqlite_autoincrement': True}
    id: Mapped[int] = mapped_column(primary_key=True, init=False, autoincrement=True)
    email: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('user_account.id'))
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())

# engine and session_factory should be application scoped - you should not need to make
# another one in your application.

engine = create_engine('sqlite://', echo=True)
session_factory = sessionmaker(bind=engine)
# session = session_factory()

# print(session)

# result = session.execute(text("select 'hello world'"))
# print(result.first())



with engine.begin() as conn:
    Base.metadata.create_all(conn)


with session_factory.begin() as sess:
    sess.execute(
        insert(User), [
               {'name': 'Andrew', 'fullname': 'Andrew Mathenge'},
               {'name': 'Tony', 'fullname': 'Tony Mwai'},
               {'name': 'Spongebob', 'fullname': 'Spongebob Squarepants'},
               {'name': 'Peter', 'fullname': 'Peter Wolf'},
               {'name': 'Julius', 'fullname': 'Julius Caesar'}
        ]
    )
    sess.execute(
        insert(Address), [
            {'user_id': 1, 'email': 'andrew@email.com'},
            {'user_id': 2, 'email': 'tony@email.com'},
            {'user_id': 2, 'email': 'tm@home.org'},
            {'user_id': 3, 'email': 'sponge@bob.com'},
            {'user_id': 4, 'email': 'peter@wolf.com'},
            {'user_id': 5, 'email': 'julius.c@rome.it'},
            {'user_id': 5, 'email': 'jc@rome.org'}
        ]
    )

# spongebob = User('Spongebob', 'Spongebob Squarepants')

# print(spongebob)