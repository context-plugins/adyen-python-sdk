from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.schedule_type1 import ScheduleType1OrStr


class Schedule2(SdkBaseModel):
    type_: ScheduleType1OrStr = Field(alias="type")
    """The type of schedule at which the top up is executed.
    * **weekdays**: pull in funds Monday-Friday at 07:00 AM in the local timezone of the balance account.

    * **weekly**: pull in funds every Monday at 07:00 AM in the local timezone of the balance account.

    * **monthly**: pull in funds every first of the month at 07:00 AM in the local timezone of the balance account.
    * **null** (default): continuous monitoring."""


class Schedule2Dict(TypedDict):
    type_: ScheduleType1OrStr
