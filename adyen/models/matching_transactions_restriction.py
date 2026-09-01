from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MatchingTransactionsRestriction(SdkBaseModel):
    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[int] = UNSET
    """The number of transactions."""


class MatchingTransactionsRestrictionDict(TypedDict):
    operation: str
    value: NotRequired[int]
