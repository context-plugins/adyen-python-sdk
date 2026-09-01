from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BoardingTokenRequest(SdkBaseModel):
    boarding_request_token: str = Field(alias="boardingRequestToken")
    """The boardingToken request token."""


class BoardingTokenRequestDict(TypedDict):
    boarding_request_token: str
