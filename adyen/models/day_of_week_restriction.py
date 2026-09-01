from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.value1 import Value1OrStr


class DayOfWeekRestriction(SdkBaseModel):
    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[Value1OrStr]] = UNSET
    """List of days of the week.

    Possible values: **monday**, **tuesday**, **wednesday**, **thursday**, **friday**, **saturday**, **sunday**."""


class DayOfWeekRestrictionDict(TypedDict):
    operation: str
    value: NotRequired[list[Value1OrStr]]
