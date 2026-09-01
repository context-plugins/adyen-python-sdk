from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Frequency(str, Enum):
    """The frequency with which a shopper should be charged.

    Possible values: **adhoc**, **daily**, **weekly**, **biWeekly**, **monthly**, **quarterly**, **halfYearly**,
    **yearly**., The frequency with which a shopper should be charged.

    Possible values: **daily**, **weekly**, **biWeekly**, **monthly**, **quarterly**, **halfYearly**, **yearly**."""

    ADHOC = "adhoc"
    DAILY = "daily"
    WEEKLY = "weekly"
    BI_WEEKLY = "biWeekly"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    HALF_YEARLY = "halfYearly"
    YEARLY = "yearly"

    __str__ = str.__str__


FrequencyOrStr: TypeAlias = Annotated[Frequency | str, open_enum_validator(Frequency)]
