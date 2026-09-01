from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .response11 import Response11, Response11Dict


class LogoutResponse(SdkBaseModel):
    """It conveys the result of the Logout. Content of the Logout Response message."""

    response: Response11 = Field(alias="Response")
    """Result of a message request processing."""


class LogoutResponseDict(TypedDict):
    response: Response11 | Response11Dict
