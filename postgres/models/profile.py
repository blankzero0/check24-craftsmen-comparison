from sqlalchemy import *
from sqlalchemy.orm import *
from geoalchemy2 import Geometry

Base = declarative_base()


class Profile(Base):
    __tablename__ = "profile"

    profile_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    city = Column(String)
    street = Column(String)
    house_number = Column(String)
    geog = Column(Geometry(geometry_type='POINT', srid=4326))
    max_driving_distance = Column(Integer)
    picture_score = Column(Float)
    description_score = Column(Float)
