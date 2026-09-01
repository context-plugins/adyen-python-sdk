from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BalancePlatform(SdkBaseModel):
    description: Optional[str] = UNSET
    """Your description of the balance platform."""

    id: str
    """The unique identifier of the balance platform."""

    status: Optional[str] = UNSET
    """The status of the balance platform.

    Possible values: **Active**, **Inactive**, **Closed**, **Suspended**."""


class BalancePlatformDict(TypedDict):
    description: NotRequired[str]
    id: str
    status: NotRequired[str]
