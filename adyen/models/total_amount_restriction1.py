from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount17 import Amount17, Amount17Dict


class TotalAmountRestriction1(SdkBaseModel):
    """The total amount and the operation.

    Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**,
    **lessThan**."""

    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[Amount17] = UNSET
    """The amount value and currency."""


class TotalAmountRestriction1Dict(TypedDict):
    operation: str
    value: NotRequired[Amount17Dict]
