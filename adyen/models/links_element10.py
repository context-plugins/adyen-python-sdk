from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinksElement10(SdkBaseModel):
    """The last page."""

    href: Optional[str] = UNSET


class LinksElement10Dict(TypedDict):
    href: NotRequired[str]
