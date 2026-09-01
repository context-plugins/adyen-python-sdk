from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.schedule_type1 import ScheduleType1OrStr


class PatchableSchedule(SdkBaseModel):
    type_: Optional[ScheduleType1OrStr] = Field(default=UNSET, alias="type")
    """The type of schedule at which the top up is executed.
    * **weekdays**: pull in funds Monday-Friday at 07:00 AM in the local timezone of the balance account.

    * **weekly**: pull in funds every Monday at 07:00 AM in the local timezone of the balance account.

    * **monthly**: pull in funds every first of the month at 07:00 AM in the local timezone of the balance account.
    * **null** (default): continuous monitoring."""


class PatchableScheduleDict(TypedDict):
    type_: NotRequired[ScheduleType1OrStr]
