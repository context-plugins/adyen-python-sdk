from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinksElement17(SdkBaseModel):
    """The merchant account that the webhook is configured for. Only present for merchant-level webhooks."""

    href: Optional[str] = UNSET


class LinksElement17Dict(TypedDict):
    href: NotRequired[str]
