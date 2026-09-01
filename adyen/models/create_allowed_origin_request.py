from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .links2 import Links2, Links2Dict


class CreateAllowedOriginRequest(SdkBaseModel):
    links: Optional[Links2] = Field(default=UNSET, alias="_links")
    """References to resources linked to the allowed origin."""

    domain: str
    """Domain of the allowed origin."""

    id: Optional[str] = UNSET
    """Unique identifier of the allowed origin."""


class CreateAllowedOriginRequestDict(TypedDict):
    links: NotRequired[Links2 | Links2Dict]
    domain: str
    id: NotRequired[str]
