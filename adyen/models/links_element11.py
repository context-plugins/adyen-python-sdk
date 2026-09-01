from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinksElement11(SdkBaseModel):
    """The next page. Only present if there is a next page."""

    href: Optional[str] = UNSET


class LinksElement11Dict(TypedDict):
    href: NotRequired[str]
