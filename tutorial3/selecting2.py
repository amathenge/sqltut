from main import session
from models import User

tony = session.query(User).filter_by(
    user = 'tony'
)

print(tony.first())

