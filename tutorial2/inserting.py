from tables import users
from connect import engine

# sql = users.insert().values(name='tony', fullname='tony mwai', email='t@g.com')

# with engine.connect() as conn:
#     conn.execute(sql)

#     conn.commit()

sql = users.insert()

with engine.connect() as conn:
    conn.execute(sql,[
        {'name': 'andrew', 'fullname': 'andrew mwai', 'email': 'am@gg.com'},
        {'name': 'peter', 'fullname': 'peter wolf', 'email': 'wolfman@arrg.not'},
        {'name': 'julius', 'fullname': 'julius caesar', 'email': 'jc@rome.gov'}
    ])
    conn.commit()

