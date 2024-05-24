from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL
import os

URL_DB = URL.create(
    drivername="postgresql",
    username="postgres",
    password="12345",
    database="veemdb",
    host="db",
    port="5432",
)

engine = create_engine(URL_DB)
connection = engine.connect()
metadata = MetaData()
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base(metadata=metadata)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

Base.metadata.create_all(bind=engine)
