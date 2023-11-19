from sqlalchemy import *
from sqlalchemy.orm import *

from db.postcode import Postcode
from db.profile import Profile

Base = declarative_base()


class Ranking(Base):
    __tablename__ = "ranking"

    postcode = mapped_column(String, ForeignKey(Postcode.postcode), primary_key=True)
    profile_id = mapped_column(Integer, ForeignKey(Profile.profile_id), primary_key=True)
    rank = mapped_column(Float)
