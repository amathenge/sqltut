from sqlalchemy import create_engine, text

engine = create_engine('sqlite://', echo=True)

connection = engine.connect()

with engine.connect() as connection:
    print(connection._dbapi_connection)

    stmt = text("select 'hello world' as greeting")

    result = connection.execute(stmt)

    print(result)

    row = result.first()

    print(row)
    print(row.greeting)
    print(row[0])
    print(row._mapping['greeting'])
    connection.commit()

# don't do this as in two.py
# connection.close()
