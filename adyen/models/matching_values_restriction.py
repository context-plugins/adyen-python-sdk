from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.value3 import Value3OrStr


class MatchingValuesRestriction(SdkBaseModel):
    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[Value3OrStr]] = UNSET


class MatchingValuesRestrictionDict(TypedDict):
    operation: str
    value: NotRequired[list[Value3OrStr]]
