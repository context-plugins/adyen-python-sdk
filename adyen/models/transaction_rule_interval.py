from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .duration1 import Duration1, Duration1Dict
from .enums.day_of_week import DayOfWeekOrStr
from .enums.type131 import Type131OrStr


class TransactionRuleInterval(SdkBaseModel):
    day_of_month: Optional[int] = Field(default=UNSET, alias="dayOfMonth")
    """The day of month, used when the ``duration.unit`` is **months**. If not provided, by default, this is set to
    **1**, the first day of the month."""

    day_of_week: Optional[DayOfWeekOrStr] = Field(default=UNSET, alias="dayOfWeek")
    """The day of week, used when the ``duration.unit`` is **weeks**. If not provided, by default, this is set to
    **monday**.

    Possible values: **sunday**, **monday**, **tuesday**, **wednesday**, **thursday**, **friday**."""

    duration: Optional[Duration1] = UNSET
    """The duration, which you can specify in hours, days, weeks, or months. The maximum duration is 90 days or an
    equivalent in other units. Required when the ``type`` is **rolling** or **sliding**."""

    time_of_day: Optional[str] = Field(default=UNSET, alias="timeOfDay")
    """The time of day, in **hh:mm:ss** format, used when the ``duration.unit`` is **hours**. If not provided, by
    default, this is set to **00:00:00**."""

    time_zone: Optional[str] = Field(default=UNSET, alias="timeZone")
    """The `time zone <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`__. For example,
    **Europe/Amsterdam**. By default, this is set to **UTC**."""

    type_: Type131OrStr = Field(alias="type")
    """The `type of interval <https://docs.adyen.com/issuing/transaction-rules#time-intervals>`__ during which the rule
    conditions and limits apply, and how often counters are reset.

    Possible values:
      * **perTransaction**: conditions are evaluated and the counters are reset for every transaction.
     * **daily**: the counters are reset daily at 00:00:00 CET.
     * **weekly**: the counters are reset every Monday at 00:00:00 CET.
     * **monthly**: the counters reset every first day of the month at 00:00:00 CET.
     * **lifetime**: conditions are applied to the lifetime of the payment instrument.
     * **rolling**: conditions are applied and the counters are reset based on a ``duration``. If the reset date and
            time are not provided, Adyen applies the default reset time similar to fixed intervals. For example, if the
            duration is every two weeks, the counter resets every third Monday at 00:00:00 CET.
     * **sliding**: conditions are applied and the counters are reset based on the current time and a ``duration`` that
            you specify."""


class TransactionRuleIntervalDict(TypedDict):
    day_of_month: NotRequired[int]
    day_of_week: NotRequired[DayOfWeekOrStr]
    duration: NotRequired[Duration1Dict]
    time_of_day: NotRequired[str]
    time_zone: NotRequired[str]
    type_: Type131OrStr
