from main import session
from models import User, Comment
from sqlalchemy import select

sql = select(User).where(User.user.in_(['paul', 'cathy']))

result = session.scalars(sql)

for user in result:
    print(user)

