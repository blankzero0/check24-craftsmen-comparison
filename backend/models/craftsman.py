from pydantic import BaseModel, Field


class Craftsman(BaseModel):
    id: int
    name: str
    ranking_score: float = Field(alias="rankingScore")
