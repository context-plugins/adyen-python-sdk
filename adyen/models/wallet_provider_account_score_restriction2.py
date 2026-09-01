from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WalletProviderAccountScoreRestriction2(SdkBaseModel):
    """Checks the wallet account score.

    Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**,
    **lessThan**."""

    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[int] = UNSET


class WalletProviderAccountScoreRestriction2Dict(TypedDict):
    operation: str
    value: NotRequired[int]
