from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .url import Url, UrlDict


class NotificationUrl2(SdkBaseModel):
    """The list of local and public URLs to send display notifications to when using Terminal API."""

    local_urls: Optional[list[Url]] = Field(default=UNSET, alias="localUrls")
    """One or more local URLs to send notifications to when using Terminal API."""

    public_urls: Optional[list[Url]] = Field(default=UNSET, alias="publicUrls")
    """One or more public URLs to send notifications to when using Terminal API."""


class NotificationUrl2Dict(TypedDict):
    local_urls: NotRequired[list[UrlDict]]
    public_urls: NotRequired[list[UrlDict]]
