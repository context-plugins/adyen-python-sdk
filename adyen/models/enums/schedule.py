from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Schedule(str, Enum):
    """The payout schedule for the account.

    Possible values: ``DEFAULT``, ``DAILY``, ``DAILY_US``, ``DAILY_EU``, ``DAILY_AU``, ``DAILY_SG``, ``WEEKLY``,
    ``WEEKLY_ON_TUE_FRI_MIDNIGHT``, ``BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT``, ``MONTHLY``, ``HOLD``.
    > ``HOLD`` prevents scheduled payouts, but you can still initiate payouts manually."""

    BIWEEKLY_ON_1_ST_AND_15_TH_AT_MIDNIGHT = "BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT"
    DAILY = "DAILY"
    DAILY_AU = "DAILY_AU"
    DAILY_EU = "DAILY_EU"
    DAILY_SG = "DAILY_SG"
    DAILY_US = "DAILY_US"
    HOLD = "HOLD"
    MONTHLY = "MONTHLY"
    WEEKLY = "WEEKLY"
    WEEKLY_MON_TO_FRI_AU = "WEEKLY_MON_TO_FRI_AU"
    WEEKLY_MON_TO_FRI_EU = "WEEKLY_MON_TO_FRI_EU"
    WEEKLY_MON_TO_FRI_US = "WEEKLY_MON_TO_FRI_US"
    WEEKLY_ON_TUE_FRI_MIDNIGHT = "WEEKLY_ON_TUE_FRI_MIDNIGHT"
    WEEKLY_SUN_TO_THU_AU = "WEEKLY_SUN_TO_THU_AU"
    WEEKLY_SUN_TO_THU_US = "WEEKLY_SUN_TO_THU_US"

    __str__ = str.__str__


ScheduleOrStr: TypeAlias = Annotated[Schedule | str, open_enum_validator(Schedule)]
