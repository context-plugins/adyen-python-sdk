from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ScheduleType1(str, Enum):
    """The type of schedule at which the top up is executed.
    * **weekdays**: pull in funds Monday-Friday at 07:00 AM in the local timezone of the balance account.

    * **weekly**: pull in funds every Monday at 07:00 AM in the local timezone of the balance account.

    * **monthly**: pull in funds every first of the month at 07:00 AM in the local timezone of the balance account.
    * **null** (default): continuous monitoring."""

    WEEKDAYS = "weekdays"
    WEEKLY = "weekly"
    MONTHLY = "monthly"

    __str__ = str.__str__


ScheduleType1OrStr: TypeAlias = Annotated[ScheduleType1 | str, open_enum_validator(ScheduleType1)]
