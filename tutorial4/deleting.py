from models import engine, students, db

sql = students.delete().where(students.c.lastname == 'Andree')
print(sql)

with engine.begin() as conn:
    conn.execute(sql)

