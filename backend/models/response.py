from pydantic import BaseModel
from models.craftsman import Craftsman


class Response(BaseModel):
    craftsmen: list[Craftsman]
