from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DayOfWeek(str, Enum):
    """The day of week, used when the ``duration.unit`` is **weeks**. If not provided, by default, this is set to
    **monday**.

    Possible values: **sunday**, **monday**, **tuesday**, **wednesday**, **thursday**, **friday**."""

    FRIDAY = "friday"
    MONDAY = "monday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"
    THURSDAY = "thursday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"

    __str__ = str.__str__


DayOfWeekOrStr: TypeAlias = Annotated[DayOfWeek | str, open_enum_validator(DayOfWeek)]
