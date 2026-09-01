from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SameAmountRestriction1(SdkBaseModel):
    """Checks if a user has recently sent the same amount of funds in multiple transfers.

    To use this restriction, you must:

    - Set the rule ``type`` to **velocity**.

    - Specify a time ``interval``.

    - Specify a number of ``matchingTransactions``.

    Supported operation: **equals**."""

    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[bool] = UNSET


class SameAmountRestriction1Dict(TypedDict):
    operation: str
    value: NotRequired[bool]
