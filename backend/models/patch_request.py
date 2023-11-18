from typing import Optional

from pydantic import BaseModel, Field


class PatchRequest(BaseModel):
    max_driving_distance: Optional[float] = Field(alias="maxDrivingDistance", default=None)
    profile_picture_score: Optional[float] = Field(alias="profilePictureScore", default=None)
    profile_description_score: Optional[float] = Field(alias="profileDescriptionScore", default=None)
