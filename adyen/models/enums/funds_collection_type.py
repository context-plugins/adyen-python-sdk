from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FundsCollectionType(str, Enum):
    UNSCHEDULED_REPAYMENT = "UnscheduledRepayment"
    REVOCATION = "Revocation"

    __str__ = str.__str__


FundsCollectionTypeOrStr: TypeAlias = Annotated[FundsCollectionType | str, open_enum_validator(FundsCollectionType)]
