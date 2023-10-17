from main import session
from models import User, Comment


comment = session.query(Comment).filter_by(id=19).first()

comment.comment = 'This is an updated comment'

session.commit()
