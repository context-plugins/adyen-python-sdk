from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinksElement5(SdkBaseModel):
    """The merchant account that the API credential is linked to. Only present for merchant-level API credentials."""

    href: Optional[str] = UNSET


class LinksElement5Dict(TypedDict):
    href: NotRequired[str]
