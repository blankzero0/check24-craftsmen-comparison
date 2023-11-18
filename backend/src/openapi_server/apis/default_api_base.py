# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.patch_request import PatchRequest
from openapi_server.models.patch_response import PatchResponse
from openapi_server.models.response import Response


class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    def craftman_craftman_id_patch(
        self,
        craftman_id: int,
        patch_request: PatchRequest,
    ) -> PatchResponse:
        ...


    def craftsmen_get(
        self,
        postalcode: str,
    ) -> Response:
        ...
