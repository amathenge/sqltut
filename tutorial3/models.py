from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text
from typing import List

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'sqlite_autoincrement': True}
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str]
    comments: Mapped[List['Comment']] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User: user={self.user}"

class Comment(Base):
    __tablename__ = 'comments'
    __table_args__ = {'sqlite_autoincrement': True}
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    comment: Mapped[str] = mapped_column(Text, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    user: Mapped["User"] = relationship(back_populates='comments')

    def __repr__(self) -> str:
        return f"Comment = {self.comment} by {self.user.user}"