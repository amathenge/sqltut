from tables import users
from connect import engine

# sql = users.insert().values(name='tony', fullname='tony mwai', email='t@g.com')

# with engine.connect() as conn:
#     conn.execute(sql)

#     conn.commit()

sql = users.insert()

with engine.begin() as conn:
    conn.execute(sql,[
        {'name': 'sly', 'fullname': 'sly fox', 'email': 'sf@knox.com'},
        {'name': 'riding', 'fullname': 'riding hood', 'email': 'riding@hood.not'},
        {'name': 'attila', 'fullname': 'atilla hun', 'email': 'attila@hun.gov'}
    ])

