from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinksElement12(SdkBaseModel):
    """The previous page. Only present if there is a previous page."""

    href: Optional[str] = UNSET


class LinksElement12Dict(TypedDict):
    href: NotRequired[str]
