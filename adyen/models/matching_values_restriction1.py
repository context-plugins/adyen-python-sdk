from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.value3 import Value3OrStr


class MatchingValuesRestriction1(SdkBaseModel):
    """Checks if a user has recently made multiple transfers with the specified values.

    To use this restriction, you must:

    - Set the rule ``type`` to **velocity**.

    - Specify a time ``interval``.

    - Specify a number of ``matchingTransactions``.

    Supported operation: **allMatch**.

    Supported value inputs:
    - **merchantId** and **acquirerId**
    - **amount** and **currency**
    - **merchantName**."""

    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[Value3OrStr]] = UNSET


class MatchingValuesRestriction1Dict(TypedDict):
    operation: str
    value: NotRequired[list[Value3OrStr]]
