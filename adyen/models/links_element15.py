from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinksElement15(SdkBaseModel):
    """The company account that the webhook is configured for. Only present for company-level webhooks."""

    href: Optional[str] = UNSET


class LinksElement15Dict(TypedDict):
    href: NotRequired[str]
