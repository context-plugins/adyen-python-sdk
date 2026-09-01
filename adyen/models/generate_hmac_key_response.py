from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GenerateHmacKeyResponse(SdkBaseModel):
    hmac_key: str = Field(alias="hmacKey")
    """The HMAC key generated for this webhook."""


class GenerateHmacKeyResponseDict(TypedDict):
    hmac_key: str
