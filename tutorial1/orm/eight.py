from datetime import datetime
from typing import Optional
from sqlalchemy import func, create_engine, insert, text, select, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, MappedAsDataclass

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

engine = create_engine('sqlite://', echo=True)
with engine.begin() as conn:
    Base.metadata.create_all(conn)


with engine.begin() as conn:
    conn.execute(
        insert(User), [
               {'name': 'Andrew', 'fullname': 'Andrew Mathenge'},
               {'name': 'Tony', 'fullname': 'Tony Mwai'},
               {'name': 'Spongebob', 'fullname': 'Spongebob Squarepants'},
               {'name': 'Peter', 'fullname': 'Peter Wolf'},
               {'name': 'Julius', 'fullname': 'Julius Caesar'}
        ]
    )
    conn.execute(
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

stmt = text('select name from user_account')

with engine.connect() as conn:
    result = conn.execute(stmt)

for row in result:
    print(row.name)

# another way

stmt = select(User.name)
print(stmt)

with engine.connect() as conn:
    result = conn.execute(stmt)

for row in result:
    print(row.name)

# all columns
stmt = select(User)

with engine.connect() as conn:
    result = conn.execute(stmt)

for row in result:
    print(row.id, row.name, row.fullname, row.created_at)

# few columns
stmt = select(User.id, User.name)

with engine.connect() as conn:
    result = conn.execute(stmt)

for row in result:
    print(row.id, row.name)

# address stuff:
stmt = select(Address)

with engine.connect() as conn:
    result = conn.execute(stmt)

for row in result:
    print(row.id, row.email, row.user_id, row.created_at)

# join stuff

stmt = select(User.id, User.fullname, Address.email).join_from(User,Address)
print(stmt)

with engine.connect() as conn:
    result = conn.execute(stmt)

for row in result:
    print(row.id, row.fullname, row.email)

# select people who have more than one email address

email_count = select(Address.user_id, func.count(Address.email).label('email_count')).group_by(
        Address.user_id
    ).having(func.count(Address.email) > 1).subquery()

stmt = select(User.name, email_count.c.email_count).join_from(User, email_count)

print(stmt)

with engine.connect() as conn:
    result = conn.execute(stmt)

for row in result:
    print(row.name, row.email_count)