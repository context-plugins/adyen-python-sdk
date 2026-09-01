from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FundsCollectionType2(str, Enum):
    """The type of funds collection.

    Possible values: **UnscheduledRepayment**, **Revocation**."""

    UNSCHEDULED_REPAYMENT = "UnscheduledRepayment"
    REVOCATION = "Revocation"

    __str__ = str.__str__


FundsCollectionType2OrStr: TypeAlias = Annotated[FundsCollectionType2 | str, open_enum_validator(FundsCollectionType2)]
