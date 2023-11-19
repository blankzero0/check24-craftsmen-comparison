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

    def __repr__(self):
        return "Profile(profile_id={}, first_name={}, last_name={}, city={}, street={}, \
                house_number={}, geog={}, max_driving_distance={}, picture_score={}, description_score={})" \
                .format(self.profile_id, self.first_name, self.last_name, self.city, self.street,
                        self.house_number, self.geog, self.max_driving_distance, self.picture_score, self.description_score)
