from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

Base = declarative_base()

class Postcode(Base):
    __tablename__ = "postcode"

    postcode = Column(String, primary_key=True)
    lon = Column(Double)
    lat = Column(Double)
    postcode_extension_distance_group = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __repr__(self):
        return f"Postcode(postcode={self.postcode!r}), lon={self.lon!r},postcode={self.lat!r}, postcode={self.postcode_extension_distance_group!r},postcode={self.created_at!r}, postcode={self.updated_at!r}"
