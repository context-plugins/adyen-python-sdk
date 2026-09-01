from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinksElement9(SdkBaseModel):
    """The first page."""

    href: Optional[str] = UNSET


class LinksElement9Dict(TypedDict):
    href: NotRequired[str]
