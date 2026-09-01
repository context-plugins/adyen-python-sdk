from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GenerateClientKeyResponse(SdkBaseModel):
    client_key: str = Field(alias="clientKey")
    """Generated client key"""


class GenerateClientKeyResponseDict(TypedDict):
    client_key: str
