from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.schedule import ScheduleOrStr


class PayoutScheduleResponse1(SdkBaseModel):
    """The details of the payout schedule added to the account."""

    next_scheduled_payout: Optional[RFC3339DateTime] = Field(default=UNSET, alias="nextScheduledPayout")
    """The date of the next scheduled payout."""

    schedule: Optional[ScheduleOrStr] = UNSET
    """The payout schedule for the account.

    Possible values: ``DEFAULT``, ``DAILY``, ``DAILY_US``, ``DAILY_EU``, ``DAILY_AU``, ``DAILY_SG``, ``WEEKLY``,
    ``WEEKLY_ON_TUE_FRI_MIDNIGHT``, ``BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT``, ``MONTHLY``, ``HOLD``.
    > ``HOLD`` prevents scheduled payouts, but you can still initiate payouts manually."""


class PayoutScheduleResponse1Dict(TypedDict):
    next_scheduled_payout: NotRequired[RFC3339DateTime]
    schedule: NotRequired[ScheduleOrStr]
