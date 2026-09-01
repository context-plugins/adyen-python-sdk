from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WalletProviderDeviceScore2(SdkBaseModel):
    """Wallet Provider Device Score and the operation.

    Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**,
    **lessThan**."""

    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[int] = UNSET


class WalletProviderDeviceScore2Dict(TypedDict):
    operation: str
    value: NotRequired[int]
