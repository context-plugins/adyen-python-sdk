from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Plan1(str, Enum):
    BONUS = "bonus"
    BUYNOW_PAYLATER = "buynow_paylater"
    INTERES_REFUND_PRCTG = "interes_refund_prctg"
    INTEREST_BONUS = "interest_bonus"
    NOINTERES_REFUND_PRCTG = "nointeres_refund_prctg"
    NOINTEREST_BONUS = "nointerest_bonus"
    REFUND_PRCTG = "refund_prctg"
    REGULAR = "regular"
    REVOLVING = "revolving"
    WITH_INTEREST = "with_interest"

    __str__ = str.__str__


Plan1OrStr: TypeAlias = Annotated[Plan1 | str, open_enum_validator(Plan1)]
