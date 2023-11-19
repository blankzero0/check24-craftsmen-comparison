from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

conn_string = f"postgresql://postgres@{os.environ.get('POSTGRES_HOST', 'db')}/{os.environ.get('POSTGRES_DB', 'craftsmen')}"

engine = create_engine(conn_string)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
