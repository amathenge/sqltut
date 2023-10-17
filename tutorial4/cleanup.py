# cleanup the students environment and start over.

from models import engine, metadata, students, table_exists

if table_exists('students'):
    students.drop(bind=engine, checkfirst=True)

# now recreate and insert data.
metadata.create_all(bind=engine)

# after you recreate the tables, run inserting.py to put all the data back into the database.
# note that inserting.py needs a file called dictlist.txt a text file with dictionary entries.
# this dictionary is created by dictconv.py from data.csv ()
