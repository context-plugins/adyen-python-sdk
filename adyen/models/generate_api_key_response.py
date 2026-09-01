from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GenerateApiKeyResponse(SdkBaseModel):
    api_key: str = Field(alias="apiKey")
    """The generated API key."""


class GenerateApiKeyResponseDict(TypedDict):
    api_key: str
