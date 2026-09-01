from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinksElement3(SdkBaseModel):
    """Generates a new API key. When you generate a new one, the existing key remains valid for 24 hours."""

    href: Optional[str] = UNSET


class LinksElement3Dict(TypedDict):
    href: NotRequired[str]
