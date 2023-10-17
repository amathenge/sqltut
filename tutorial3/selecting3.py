from main import session
from models import User, Comment
from sqlalchemy import select

sql = select(Comment).join(Comment.user).where(
    User.user == 'tony'
).where(
    Comment.comment == 'Hello World'
)

result = session.scalars(sql).one()

print(result)

