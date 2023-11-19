from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

conn_string = f"postgresql://postgres@db/{os.environ['POSTGRES_DB']}"

engine = create_engine(conn_string)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
