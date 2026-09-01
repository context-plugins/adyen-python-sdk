from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConfidenceScore(SdkBaseModel):
    errors: Optional[list[str]] = UNSET
    score: Optional[float] = UNSET


class ConfidenceScoreDict(TypedDict):
    errors: NotRequired[list[str]]
    score: NotRequired[float]
