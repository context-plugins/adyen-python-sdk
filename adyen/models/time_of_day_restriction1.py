from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .time_of_day import TimeOfDay, TimeOfDayDict


class TimeOfDayRestriction1(SdkBaseModel):
    """A start and end time in a time-only ISO-8601 extended offset format. Supported operations: **equals**,
    **notEquals**."""

    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[TimeOfDay] = UNSET


class TimeOfDayRestriction1Dict(TypedDict):
    operation: str
    value: NotRequired[TimeOfDayDict]
