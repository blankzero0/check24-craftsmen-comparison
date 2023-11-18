# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class Craftsman(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Craftsman - a model defined in OpenAPI

        id: The id of this Craftsman.
        name: The name of this Craftsman.
        ranking_score: The ranking_score of this Craftsman.
    """

    id: int = Field(alias="id")
    name: str = Field(alias="name")
    ranking_score: float = Field(alias="rankingScore")