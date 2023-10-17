import sqlalchemy as db

engine = db.create_engine('sqlite:///country.db')

with engine.connect() as conn:
    result = conn.execute(db.text('select * from countries'))
    print(result.all())

