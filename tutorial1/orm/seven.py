from datetime import datetime
from typing import Optional
from sqlalchemy import func, create_engine, insert, text, select
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

