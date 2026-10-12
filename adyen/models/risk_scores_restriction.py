from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .risk_scores import RiskScores, RiskScoresDict


class RiskScoresRestriction(SdkBaseModel):
    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[RiskScores] = UNSET


class RiskScoresRestrictionDict(TypedDict):
    operation: str
    value: NotRequired[RiskScoresDict]
