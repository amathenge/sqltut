from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///sample.db', echo=True)

# with engine.connect() as conn:
#     result = conn.execute(text('select "hello"'))

#     print(result.all())