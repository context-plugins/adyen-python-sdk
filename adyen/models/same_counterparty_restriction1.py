from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SameCounterpartyRestriction1(SdkBaseModel):
    """Checks if a user has recently made multiple transfers to the same counterparty.

    To use this restriction, you must:

    - Set the rule ``type`` to **velocity**.

    - Specify a time ``interval``.

    - Specify a number of ``matchingTransactions``.

    Supported operations: **equals**."""

    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[bool] = UNSET


class SameCounterpartyRestriction1Dict(TypedDict):
    operation: str
    value: NotRequired[bool]
