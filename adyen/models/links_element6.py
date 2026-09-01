from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinksElement6(SdkBaseModel):
    """Link to the resource itself."""

    href: Optional[str] = UNSET


class LinksElement6Dict(TypedDict):
    href: NotRequired[str]
