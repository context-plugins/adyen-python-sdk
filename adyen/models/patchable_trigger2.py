from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .patchable_amount_dto1 import PatchableAmountDto1, PatchableAmountDto1Dict
from .patchable_schedule import PatchableSchedule, PatchableScheduleDict


class PatchableTrigger2(SdkBaseModel):
    """The condition that triggers the top-up. This can be a recurring schedule or a minimum balance threshold."""

    schedule: OptionalNullable[PatchableSchedule] = UNSET
    """Contains the details about the schedule that determines when the top up is executed."""

    threshold: Optional[PatchableAmountDto1] = UNSET
    """The balance threshold that triggers the top-up. If the balance falls below this amount, a top-up is initiated."""


class PatchableTrigger2Dict(TypedDict):
    schedule: NotRequired[PatchableSchedule | PatchableScheduleDict | None]
    threshold: NotRequired[PatchableAmountDto1 | PatchableAmountDto1Dict]
