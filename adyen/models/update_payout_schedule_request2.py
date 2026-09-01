from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.action import ActionOrStr
from .enums.schedule1 import Schedule1OrStr


class UpdatePayoutScheduleRequest2(SdkBaseModel):
    """The details of the payout schedule to which the account must be updated."""

    action: Optional[ActionOrStr] = UNSET
    """Direction on how to handle any payouts that have already been scheduled.

    Possible values:
    * ``CLOSE``: close the existing batch of payouts.
    * ``UPDATE``: reschedule the existing batch to the new schedule.
    * ``NOTHING`` (**default**): allow the payout to proceed."""

    reason: Optional[str] = UNSET
    """The reason for the payout schedule update.
    > This field is required when the ``schedule`` parameter is set to ``HOLD``."""

    schedule: Schedule1OrStr
    """The new payout schedule for the account.

    Possible values: ``DEFAULT``, ``DAILY``, ``DAILY_US``, ``DAILY_EU``, ``DAILY_AU``, ``DAILY_SG``, ``WEEKLY``,
    ``WEEKLY_ON_TUE_FRI_MIDNIGHT``, ``BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT``, ``MONTHLY``, ``HOLD``.
    > ``HOLD`` prevents scheduled payouts, but you can still initiate payouts manually."""


class UpdatePayoutScheduleRequest2Dict(TypedDict):
    action: NotRequired[ActionOrStr]
    reason: NotRequired[str]
    schedule: Schedule1OrStr
