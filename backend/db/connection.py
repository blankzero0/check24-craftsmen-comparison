from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from pathlib import Path

dotenv_path = Path('../mysql/mysql.env')
load_dotenv(dotenv_path=dotenv_path)

conn_string = f"postgresql://postgres@db/{os.environ['POSTGES_DB']}"

engine = create_engine(conn_string)
conn = engine.connect()

Session = sessionmaker(bind=conn)
session = Session()
