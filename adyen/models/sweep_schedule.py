from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type62 import Type62OrStr


class SweepSchedule(SdkBaseModel):
    cron_expression: Optional[str] = Field(default=UNSET, alias="cronExpression")
    """A `cron expression <https://en.wikipedia.org/wiki/Cron#CRON_expression>`__ that is used to set the sweep
    schedule. The schedule uses the time zone of the balance account. For example, **30 17 * * MON** schedules a sweep
    every Monday at 17:30.

    The expression must have five values separated by a single space in the following order:

    * Minute: **0-59**

    * Hour: **0-23**

    * Day of the month: **1-31**

    * Month: **1-12** or **JAN-DEC**

    * Day of the week: **0-7** (0 and 7 are Sunday) or **MON-SUN**.

    The following non-standard characters are supported: **&ast;**, **L**, **#**, **W** and **/**. See `crontab guru
    <https://crontab.guru/>`__ for more examples.

    Required when ``type`` is **cron**."""

    type_: Type62OrStr = Field(alias="type")
    """The schedule type.

    Possible values:

    * **cron**: push out funds based on a ``cronExpression``.

    * **daily**: push out funds daily at 07:00 AM CET.

    * **weekly**: push out funds every Monday at 07:00 AM CET.

    * **monthly**: push out funds every first of the month at 07:00 AM CET.

    * **balance**: execute the sweep instantly if the ``triggerAmount`` is reached."""


class SweepScheduleDict(TypedDict):
    cron_expression: NotRequired[str]
    type_: Type62OrStr
