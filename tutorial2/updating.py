from tables import users
from connect import engine

sql = users.update().where(users.c.name == 'tony').values(name='anthony')

print(sql)

with engine.connect() as conn:
    conn.execute(sql)
    conn.commit()

