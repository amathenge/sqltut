import sqlalchemy as db
engine = db.create_engine('sqlite:///college.db', echo = True)
conn = engine.connect()

meta = db.MetaData()

students = db.Table(
   'students', meta, 
   db.Column('id', db.Integer, primary_key=True, autoincrement=True), 
   db.Column('firstname', db.String(64)), 
   db.Column('lastname', db.String(64)),
   db.Column('email', db.String(64)),
   db.Column('phone', db.String(12)),
   sqlite_autoincrement=True
)

# to create all the tables, you do this.
# meta.create_all(engine)
# print("these are columns in our table %s" %(students.columns.keys()))

# check to see if a table exists
def table_exists(engine, tablename):
    print(f'table {tablename} already exists')
    return db.inspect(engine).has_table(tablename)

# but to create only one table, it's easier to do this.
# if table_exists(engine, 'students'):
#     students.drop(engine)

# students.create(engine)

print("these are columns in our table %s" %(students.columns.keys()))

ins = students.insert().values(
    firstname = 'Tony',
    lastname = 'Mathenge',
    email = 'tony@email.com',
    phone = '9051234567'
)
# .returning(students.c.id, students.c.firstname, students.c.lastname)

print(ins)
conn.execute(ins)
conn.commit()

# with engine.begin() as conn:
#     result = conn.execute(ins)

ins = students.insert().values (
    firstname = 'Andrew',
    lastname = 'Mwai',
    email = 'andrew@email.com',
    phone = '7029008765'
)

print(ins)
conn.execute(ins)
conn.commit()

# with engine.begin() as conn:
#     result = conn.execute(ins)
