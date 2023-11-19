from sqlalchemy import *
from sqlalchemy.orm import *
from geoalchemy2 import Geometry

Base = declarative_base()


class Postcode(Base):
    __tablename__ = "postcode"

    postcode = Column(String, primary_key=True)
    geog = Column(Geometry(geometry_type='POINT', srid=4326))
    dist_group = Column(String)

    def __repr__(self):
        return "Postcode(postcode = {}, geog = {}, dist_group = {}" \
               .format(self.postcode, self.geog, self.dist_group)
