from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .response11 import Response11, Response11Dict


class AdminResponse(SdkBaseModel):
    """It conveys the result of the Custom Admin. Content of the Custom Admin Response message."""

    response: Response11 = Field(alias="Response")
    """Result of a message request processing."""


class AdminResponseDict(TypedDict):
    response: Response11Dict
