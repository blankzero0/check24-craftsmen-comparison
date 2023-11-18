from pydantic import BaseModel, Field
from models.patch_response_updated import PatchResponseUpdated


class PatchResponse(BaseModel):
    id: int
    updated: PatchResponseUpdated
