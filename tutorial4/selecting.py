from models import engine, students, db

# see column operators that can be used in the select.where() clause
# https://docs.sqlalchemy.org/en/20/core/operators.html

sql = students.select()
print(sql)

with engine.connect() as conn:
    results = conn.execute(sql)

    for row in results:
        print(row)

sql = db.text('select id, name from students')

with engine.connect() as conn:
    results = conn.execute(sql)

    for row in results:
        print(row)

sql = db.text('select name, lastname from students where lastname like :x')

with engine.connect() as conn:
    results = conn.execute(sql, {'x':'%ath%'})

    for row in results:
        print(row)

# with this LIKE clause, you have to provide the '%' wrapped.
sql = students.select().where(students.c.lastname.like('%ath%'))
print(sql)

with engine.connect() as conn:
    results = conn.execute(sql)

    for row in results:
        print(row)

sql = students.select().where(students.c.name.in_(['tony', 'andrew']))
print(sql)

with engine.connect() as conn:
    results = conn.execute(sql)

    for row in results:
        print(row)

# this is a better LIKE clause
sql = students.select().where(students.c.lastname.contains('ath'))
print(sql)

with engine.connect() as conn:
    results = conn.execute(sql)

    for row in results:
        print(row)

# using match() to find stuff. THIS DOES NOT WORK WITH SQLITE
# sql = students.select().where(students.c.lastname.match('ath'))
# print(sql)

# with engine.connect() as conn:
#     results = conn.execute(sql)

#     for row in results:
#         print(row)

# getting back specific columns
sql = students.select().with_only_columns(students.c.name, students.c.lastname)
print(sql)

with engine.connect() as conn:
    results = conn.execute(sql)

    for row in results:
        print(row)

# getting back specific columns and using LIKE
sql = students.select().with_only_columns(students.c.name, students.c.lastname).where(
    students.c.lastname.contains('ath')
)
print(sql)

with engine.connect() as conn:
    results = conn.execute(sql)

    for row in results:
        print(row)

# the where does not have to be in the selected list.
sql = students.select().with_only_columns(
    students.c.name
).where(
    students.c.id > 2
)
print(sql)

with engine.connect() as conn:
    results = conn.execute(sql)

    for row in results:
        print(row)


