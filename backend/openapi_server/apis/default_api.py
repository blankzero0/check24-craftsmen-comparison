# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.default_api_base import BaseDefaultApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.patch_request import PatchRequest
from openapi_server.models.patch_response import PatchResponse
from openapi_server.models.response import Response


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.patch(
    "/craftman/{craftman_id}",
    responses={
        200: {"model": PatchResponse, "description": "Craftsman updated successfully"},
    },
    tags=["default"],
    summary="Updates a craftsman&#39;s profile information",
    response_model_by_alias=True,
)
async def craftman_craftman_id_patch(
    craftman_id: int = Path(None, description="Unique ID of the craftsman"),
    patch_request: PatchRequest = Body(None, description=""),
) -> PatchResponse:
    ...


@router.get(
    "/craftsmen",
    responses={
        200: {"model": Response, "description": "List of craftsmen"},
    },
    tags=["default"],
    summary="Retrieves a list of craftsmen based on postal code",
    response_model_by_alias=True,
)
async def craftsmen_get(
    postalcode: str = Query(None, description="Postal code to filter craftsmen"),
) -> Response:
    ...
