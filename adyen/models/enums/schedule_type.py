from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ScheduleType(str, Enum):
    WEEKDAYS = "weekdays"
    WEEKLY = "weekly"
    MONTHLY = "monthly"

    __str__ = str.__str__


ScheduleTypeOrStr: TypeAlias = Annotated[ScheduleType | str, open_enum_validator(ScheduleType)]
