from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .response11 import Response11, Response11Dict


class AdminResponse2(SdkBaseModel):
    """Content of the Admin Response message."""

    response: Response11 = Field(alias="Response")
    """Result of a message request processing."""


class AdminResponse2Dict(TypedDict):
    response: Response11 | Response11Dict
