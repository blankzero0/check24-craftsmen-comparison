from sqlalchemy import *
from sqlalchemy.orm import *

Base = declarative_base()


class ServiceProviderProfile(Base):
    __tablename__ = "service_provider_profile"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    city = Column(String)
    street = Column(String)
    house_number = Column(String)
    lon = Column(Double)
    lat = Column(Double)
    max_driving_distance = Column(Integer)

    def __repr__(self) -> str:
        return f"ServiceProviderProfile(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, city={self.city!r}, street={self.street!r}, house_number={self.house_number!r}, lon={self.lon!r}, lat={self.lat!r}, max_driving_distance={self.max_driving_distance!r})"
