from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.value1 import Value1OrStr


class DayOfWeekRestriction1(SdkBaseModel):
    """List of week days and the operation. Supported operations: **anyMatch**, **noneMatch**."""

    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[Value1OrStr]] = UNSET
    """List of days of the week.

    Possible values: **monday**, **tuesday**, **wednesday**, **thursday**, **friday**, **saturday**, **sunday**."""


class DayOfWeekRestriction1Dict(TypedDict):
    operation: str
    value: NotRequired[list[Value1OrStr]]
