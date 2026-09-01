from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinksElement19(SdkBaseModel):
    """Test the webhook setup."""

    href: Optional[str] = UNSET


class LinksElement19Dict(TypedDict):
    href: NotRequired[str]
