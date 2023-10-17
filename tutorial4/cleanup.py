# cleanup the students environment and start over.

from models import engine, metadata, students, table_exists

if table_exists('students'):
    students.drop(bind=engine, checkfirst=True)

# now recreate and insert data.
metadata.create_all(bind=engine)

