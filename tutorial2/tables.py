from sqlalchemy import Table, MetaData, Column, String, Text, Integer, ForeignKey


metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(25), nullable=False),
    Column("fullname", Text),
    Column("email", String(64))
)

comments = Table(
    "comments",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("comment", Text, nullable=False),
    Column("user_id", ForeignKey("users.id"))
)