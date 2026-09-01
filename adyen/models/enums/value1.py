from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Value1(str, Enum):
    FRIDAY = "friday"
    MONDAY = "monday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"
    THURSDAY = "thursday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"

    __str__ = str.__str__


Value1OrStr: TypeAlias = Annotated[Value1 | str, open_enum_validator(Value1)]
