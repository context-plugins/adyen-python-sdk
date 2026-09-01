from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinksElement13(SdkBaseModel):
    """The current page."""

    href: Optional[str] = UNSET


class LinksElement13Dict(TypedDict):
    href: NotRequired[str]
