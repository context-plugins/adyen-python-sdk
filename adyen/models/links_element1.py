from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinksElement1(SdkBaseModel):
    """List of allowed origins."""

    href: Optional[str] = UNSET


class LinksElement1Dict(TypedDict):
    href: NotRequired[str]
