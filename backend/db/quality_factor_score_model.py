from sqlalchemy import *
from sqlalchemy.orm import *

Base = declarative_base()


class QualityFactorScore(Base):
    __tablename__ = "quality_factor_score"

    profile_id = Column(Integer, primary_key=True)
    profile_picture_score = Column(Float)
    profile_description_score = Column(Float)

    def __repr__(self) -> str:
        return f"QualityFactorScore(id={self.id!r}, profile_picture_score={self.profile_picture_score!r}, profile_description_score={self.profile_description_score!r})"