from models import engine, students, db

sql = students.update().where(students.c.lastname == 'Goodrick').values(lastname = 'Goodrick-Updated')
print(sql)

with engine.begin() as conn:
    conn.execute(sql)

