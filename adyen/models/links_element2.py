from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinksElement2(SdkBaseModel):
    """Company account that the API credential is linked to. Only present for company-level webhooks."""

    href: Optional[str] = UNSET


class LinksElement2Dict(TypedDict):
    href: NotRequired[str]
