# coding: utf-8

"""
    Craftsmen Service API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from fastapi import FastAPI

from openapi_server.apis.default_api import router as DefaultApiRouter

app = FastAPI(
    title="Craftsmen Service API",
    description="No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)",
    version="1.0.0",
)

app.include_router(DefaultApiRouter)
