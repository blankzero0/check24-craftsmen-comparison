from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from db import SessionLocal
from db.models import Profile, Ranking

from models.craftsman import Craftsman
from models.patch_response import PatchResponse
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


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/craftman")
def get_postalcode(postalcode: str, below: float | None, db: Session = Depends(get_db)) -> Response:

    statement = (select(Profile.profile_id, Profile.first_name, Profile.last_name, Ranking.rank)
                 .join_from(Profile, Ranking)
                 .filter(Ranking.postcode == postalcode)
                 .order_by(Ranking.rank.desc())
                 .limit(20))

    if below:
        statement = statement.filter(Ranking.rank < below)

    craftsmen = [Craftsman(id=row[0], name=f'{row[1]} {row[2]}', ranking_score=row[3]) for row in db.execute(statement)]

    return Response(craftsmen=craftsmen, below=craftsmen[-1].ranking_score)


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
def update_craftsman(craftman_id: int, db: Session = Depends(get_db)) -> PatchResponse:
    pass
