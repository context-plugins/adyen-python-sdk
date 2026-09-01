from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TimeOfDay(SdkBaseModel):
    end_time: Optional[str] = Field(default=UNSET, alias="endTime")
    """The end time in a time-only ISO-8601 extended offset format. For example: **08:00:00+02:00**,
    **22:30:00-03:00**."""

    start_time: Optional[str] = Field(default=UNSET, alias="startTime")
    """The start time in a time-only ISO-8601 extended offset format. For example: **08:00:00+02:00**,
    **22:30:00-03:00**."""


class TimeOfDayDict(TypedDict):
    end_time: NotRequired[str]
    start_time: NotRequired[str]
