from connect import engine
from tables import users, comments, metadata

print('>>> creating tables <<<')
metadata.create_all(bind=engine)
print('>>> all tables created <<<')

