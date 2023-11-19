from sqlalchemy import *
from sqlalchemy.orm import *
from geoalchemy2 import Geometry

Base = declarative_base()


class Postcode(Base):
    __tablename__ = "postcode"

    postcode = mapped_column(String, primary_key=True)
    geog = mapped_column(Geometry(geometry_type='POINT', srid=4326))
    dist_group = mapped_column(String)
