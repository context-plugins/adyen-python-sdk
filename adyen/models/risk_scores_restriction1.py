from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .risk_scores import RiskScores, RiskScoresDict


class RiskScoresRestriction1(SdkBaseModel):
    """Risk scores provided by specific sources. The same operation applies to all scores.

    Current sources available: **visa**, **mastercard**

    Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**,
    **lessThan**."""

    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[RiskScores] = UNSET


class RiskScoresRestriction1Dict(TypedDict):
    operation: str
    value: NotRequired[RiskScoresDict]
