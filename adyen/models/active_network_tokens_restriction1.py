from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ActiveNetworkTokensRestriction1(SdkBaseModel):
    """The total number of tokens that a card can have across different kinds of digital wallets on the user's phones,
    watches, or other wearables.

    Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**,
    **lessThan**."""

    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[int] = UNSET
    """The number of tokens."""


class ActiveNetworkTokensRestriction1Dict(TypedDict):
    operation: str
    value: NotRequired[int]
