import sqlalchemy as db

engine = db.create_engine('sqlite:///sample.db', echo=True)
metadata = db.MetaData()

students = db.Table(
    'students',
    metadata,
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('firstname', db.String(32), nullable=False),
    db.Column('lastname', db.String(128)),
    db.Column('email', db.String(32)),
    db.Column('phone', db.String(16)),
    db.Column('notes', db.Text),
    sqlite_autoincrement=True
)

def table_exists(tablename):
    return db.inspect(engine).has_table(tablename)

if not table_exists('students'):
    metadata.create_all(bind=engine)

