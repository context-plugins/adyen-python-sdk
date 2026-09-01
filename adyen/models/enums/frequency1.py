from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Frequency1(str, Enum):
    """The frequency of payouts initiated by this payout schedule.

    Possible values:
    * daily
    * weekdays
    * weekly
    * monthly

    Default value: The ``defaultFrequency`` from the balance platform schedule that you are applying."""

    DAILY = "daily"
    WEEKLY = "weekly"
    WEEKDAYS = "weekdays"
    MONTHLY = "monthly"

    __str__ = str.__str__


Frequency1OrStr: TypeAlias = Annotated[Frequency1 | str, open_enum_validator(Frequency1)]
