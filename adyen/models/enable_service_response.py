from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .response11 import Response11, Response11Dict


class EnableServiceResponse(SdkBaseModel):
    """It conveys the result of the Enable Service processing. Content of the Enable Service Response message."""

    response: Response11 = Field(alias="Response")
    """Result of a message request processing."""


class EnableServiceResponseDict(TypedDict):
    response: Response11 | Response11Dict
