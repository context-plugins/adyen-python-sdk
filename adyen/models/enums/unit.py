from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Unit(str, Enum):
    """The unit of time. You can only use **minutes** and **hours** if the ``interval.type`` is **sliding**.

    Possible values: **minutes**, **hours**, **days**, **weeks**, or **months**"""

    DAYS = "days"
    HOURS = "hours"
    MINUTES = "minutes"
    MONTHS = "months"
    WEEKS = "weeks"

    __str__ = str.__str__


UnitOrStr: TypeAlias = Annotated[Unit | str, open_enum_validator(Unit)]
