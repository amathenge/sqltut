from models import User, Comment
from main import session

user1 = User(
    user = 'tony',
    email = 'tony@tiger.com',
    comments = [
        Comment(comment='Hello World'),
        Comment(comment='Please Subscribe')
    ]
)

user2 = User(
    user = 'julius',
    email = 'jc@rome.gov',
    comments = [
        Comment(comment='This is Julius'),
        Comment(comment='Caesar was here')
    ]
)

paul = User(
    user = 'paul',
    email = 'paul@church.gov',
    comments = [
        Comment(comment='This is Paul, formerly Saul'),
        Comment(comment='Get real, or not')
    ]
)

cathy = User(
    user = 'cathy',
    email = 'cathy@gym.org',
)

session.add_all([user1, user2, paul, cathy])

session.commit()

