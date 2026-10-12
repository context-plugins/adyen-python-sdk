from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .url import Url, UrlDict


class EventUrl3(SdkBaseModel):
    """The list of local and public URLs to send notifications to when using local integrations."""

    event_local_urls: Optional[list[Url]] = Field(default=UNSET, alias="eventLocalUrls")
    """One or more local URLs to send event notifications to when using Terminal API."""

    event_public_urls: Optional[list[Url]] = Field(default=UNSET, alias="eventPublicUrls")
    """One or more public URLs to send event notifications to when using Terminal API."""


class EventUrl3Dict(TypedDict):
    event_local_urls: NotRequired[list[UrlDict]]
    event_public_urls: NotRequired[list[UrlDict]]
