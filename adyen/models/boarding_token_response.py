from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BoardingTokenResponse(SdkBaseModel):
    boarding_token: str = Field(alias="boardingToken")
    """The boarding token that allows the Payments App to board."""

    installation_id: str = Field(alias="installationId")
    """The unique identifier of the Payments App instance."""


class BoardingTokenResponseDict(TypedDict):
    boarding_token: str
    installation_id: str
