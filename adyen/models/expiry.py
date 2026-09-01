from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Expiry(SdkBaseModel):
    month: Optional[str] = UNSET
    """The month in which the card will expire."""

    year: Optional[str] = UNSET
    """The year in which the card will expire."""


class ExpiryDict(TypedDict):
    month: NotRequired[str]
    year: NotRequired[str]
