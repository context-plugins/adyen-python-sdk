from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RiskScores(SdkBaseModel):
    mastercard: Optional[int] = UNSET
    """Transaction risk score provided by Mastercard. Values provided by Mastercard range between 0 (lowest risk) to 998
    (highest risk)."""

    visa: Optional[int] = UNSET
    """Transaction risk score provided by Visa. Values provided by Visa range between 01 (lowest risk) to 99 (highest
    risk)."""


class RiskScoresDict(TypedDict):
    mastercard: NotRequired[int]
    visa: NotRequired[int]
