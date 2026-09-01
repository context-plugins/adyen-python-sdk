from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinksElement4(SdkBaseModel):
    """Generates a new client key, used to authenticate client-side requests. When you generate a new one, the existing
    key remains valid for 24 hours."""

    href: Optional[str] = UNSET


class LinksElement4Dict(TypedDict):
    href: NotRequired[str]
