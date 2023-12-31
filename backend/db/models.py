from sqlalchemy import *
from sqlalchemy.orm import *
from geoalchemy2 import Geometry

Base = declarative_base()


class Postcode(Base):
    __tablename__ = "postcode"

    postcode = mapped_column(String, primary_key=True)
    geog = mapped_column(Geometry(geometry_type='POINT', srid=4326))
    dist_group = mapped_column(String)


class Profile(Base):
    __tablename__ = "profile"

    profile_id = mapped_column(Integer, primary_key=True)
    first_name = mapped_column(String)
    last_name = mapped_column(String)
    city = mapped_column(String)
    street = mapped_column(String)
    house_number = mapped_column(String)
    geog = mapped_column(Geometry(geometry_type='POINT', srid=4326))
    max_driving_distance = mapped_column(Integer)
    picture_score = mapped_column(Float)
    description_score = mapped_column(Float)


class Ranking(Base):
    __tablename__ = "ranking"

    postcode = mapped_column(String, ForeignKey(Postcode.postcode), primary_key=True)
    profile_id = mapped_column(Integer, ForeignKey(Profile.profile_id), primary_key=True)
    rank = mapped_column(Float)
