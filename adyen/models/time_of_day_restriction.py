from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .time_of_day import TimeOfDay, TimeOfDayDict


class TimeOfDayRestriction(SdkBaseModel):
    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[TimeOfDay] = UNSET


class TimeOfDayRestrictionDict(TypedDict):
    operation: str
    value: NotRequired[TimeOfDayDict]
