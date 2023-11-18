from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from pathlib import Path

from db.postcode_model import *
# from quality_factor_score_model import *

dotenv_path = Path('../mysql/mysql.env')
load_dotenv(dotenv_path=dotenv_path)

conn_string = f"mysql+mysqlconnector://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@localhost/{os.getenv('MYSQL_DATABASE')}"

engine = create_engine(conn_string)
conn = engine.connect()

Session = sessionmaker(bind=conn)
session = Session()

# TEST CODE
"""
print("SELECT ALL")
postcode = session.query(Postcode).all()
for p in postcode:
    print(p)
"""
