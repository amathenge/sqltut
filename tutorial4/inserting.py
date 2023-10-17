from models import engine, students, db
import ast

# sql = students.insert().values(name='tony', lastname='mathenge')
# print(f"sql = {sql}")
# print(f"params = {sql.compile().params}")

# when you use connect() you need to commit()
# with engine.connect() as conn:
#     conn.execute(sql)
#     conn.commit()

# read studentdata from file
o = open('dictlist.txt', 'r')
student_data = []
rowcount = 0
for row in o:
    # skip the header column
    if rowcount > 0:
        student_data.append(ast.literal_eval(row.strip()))
    rowcount += 1
o.close()

sql = students.insert().values(student_data)
print(sql)

# when you use begin() you don't need to commit()
with engine.begin() as conn:
    conn.execute(sql)

