from tables import users
from connect import engine

sql = users.delete().where(users.c.name == 'sly')

print(sql)

with engine.begin() as conn:
    conn.execute(sql)

