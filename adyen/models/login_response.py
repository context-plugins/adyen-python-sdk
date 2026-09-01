from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .poisystem_data1 import PoisystemData1, PoisystemData1Dict
from .response11 import Response11, Response11Dict


class LoginResponse(SdkBaseModel):
    """It conveys Information related to the Login to process. Content of the Login Response message."""

    response: Response11 = Field(alias="Response")
    """Result of a message request processing."""

    poi_system_data: Optional[PoisystemData1] = Field(default=UNSET, alias="POISystemData")
    """Information related to the POI System. Returned if the response result is Success."""

    token_request_status: Optional[bool] = Field(default=UNSET, alias="TokenRequestStatus")
    """If token is managed by the POI, the status of the token request."""


class LoginResponseDict(TypedDict):
    response: Response11 | Response11Dict
    poi_system_data: NotRequired[PoisystemData1 | PoisystemData1Dict]
    token_request_status: NotRequired[bool]
