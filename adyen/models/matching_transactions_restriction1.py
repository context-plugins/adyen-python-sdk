from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MatchingTransactionsRestriction1(SdkBaseModel):
    """The number of transactions and the operation.

    Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**,
    **lessThan**."""

    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[int] = UNSET
    """The number of transactions."""


class MatchingTransactionsRestriction1Dict(TypedDict):
    operation: str
    value: NotRequired[int]
