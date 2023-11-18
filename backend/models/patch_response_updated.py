from pydantic import BaseModel, Field


class PatchResponseUpdated(BaseModel):
    max_driving_distance: float = Field(alias="maxDrivingDistance")
    profile_picture_score: float = Field(alias="profilePictureScore")
    profile_description_score: float = Field(alias="profileDescriptionScore")
