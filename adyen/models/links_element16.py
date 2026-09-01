from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinksElement16(SdkBaseModel):
    """Generate an HMAC key."""

    href: Optional[str] = UNSET


class LinksElement16Dict(TypedDict):
    href: NotRequired[str]
