from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .url import Url, UrlDict


class EventUrl(SdkBaseModel):
    event_local_urls: Optional[list[Url]] = Field(default=UNSET, alias="eventLocalUrls")
    """One or more local URLs to send event notifications to when using Terminal API."""

    event_public_urls: Optional[list[Url]] = Field(default=UNSET, alias="eventPublicUrls")
    """One or more public URLs to send event notifications to when using Terminal API."""


class EventUrlDict(TypedDict):
    event_local_urls: NotRequired[list[UrlDict]]
    event_public_urls: NotRequired[list[UrlDict]]
