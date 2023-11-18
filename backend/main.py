from fastapi import FastAPI

from db.connection import session
from db.postcode_model import Postcode
from db.service_provider_profile_model import ServiceProviderProfile

from models.craftsman import Craftsman
from models.response import Response

app = FastAPI()

"""
interface Craftsman {
    id: number;
    name: string; // firstname + lastname
    rankingScore: number;
}

interface Response {
    craftsmen: Craftsman[];
}
"""


@app.get("/craftman?postalcode={postalcode}", response_model=Response)
def get_postalcode(postalcode: str):
    craftsman_list: list[Craftsman] = []

    return {"craftsmen": craftsman_list}


"""
interface PatchRequest {
  // At least one of the attributes should be defined
  maxDrivingDistance?: number;
  profilePictureScore?: number;
  profileDescriptionScore?: number;
}

interface PatchResponse {
  id: number;
  updated: {
    maxDrivingDistance: number;
    profilePictureScore: number;
    profileDescriptionScore: number;
  }
}
"""


@app.patch("/craftman/{craftman_id}")
def update_craftsman(craftman_id: int):
    pass
