from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Url(SdkBaseModel):
    encrypted: Optional[bool] = UNSET
    """Indicates if the message sent to this URL should be encrypted."""

    password: Optional[str] = UNSET
    """The password for authentication of the notifications."""

    url: Optional[str] = UNSET
    """The URL in the format: http(s)://domain.com."""

    username: Optional[str] = UNSET
    """The username for authentication of the notifications."""


class UrlDict(TypedDict):
    encrypted: NotRequired[bool]
    password: NotRequired[str]
    url: NotRequired[str]
    username: NotRequired[str]
