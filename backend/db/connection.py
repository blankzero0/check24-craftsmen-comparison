from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config
from postcode_model import *

conn_string = f"mysql+mysqlconnector://{config.DB_USERNAME}:{config.DB_PASSWORD}@{config.DB_ADDRESS}/{config.DB_DATABASE}"

engine = create_engine(conn_string)
conn = engine.connect()

Session = sessionmaker(bind=conn)
session = Session()
