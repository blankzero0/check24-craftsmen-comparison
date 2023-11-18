# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.patch_request import PatchRequest  # noqa: F401
from openapi_server.models.patch_response import PatchResponse  # noqa: F401
from openapi_server.models.response import Response  # noqa: F401


def test_craftman_craftman_id_patch(client: TestClient):
    """Test case for craftman_craftman_id_patch

    Updates a craftsman's profile information
    """
    patch_request = {"profile_picture_score":6.027456183070403,"profile_description_score":1.4658129805029452,"max_driving_distance":0.8008281904610115}

    headers = {
    }
    response = client.request(
        "PATCH",
        "/craftman/{craftman_id}".format(craftman_id=56),
        headers=headers,
        json=patch_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_craftsmen_get(client: TestClient):
    """Test case for craftsmen_get

    Retrieves a list of craftsmen based on postal code
    """
    params = [("postalcode", 'postalcode_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/craftsmen",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

