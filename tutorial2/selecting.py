from tables import users
from connect import engine

sql = users.select()

print(sql)

with engine.connect() as conn:
    result = conn.execute(sql)

    for row in result:
        print(row)


sql = users.select().where(users.c.email.contains('.com'))

print(sql)

with engine.connect() as conn:
    result = conn.execute(sql)

    for row in result:
        print(row)

sql = users.select().where(users.c.fullname == 'tony mwai')

print(sql)

with engine.connect() as conn:
    result = conn.execute(sql)

    for row in result:
        print(row)

