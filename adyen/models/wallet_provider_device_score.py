from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WalletProviderDeviceScore(SdkBaseModel):
    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[int] = UNSET


class WalletProviderDeviceScoreDict(TypedDict):
    operation: str
    value: NotRequired[int]
