from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FundingSource9(str, Enum):
    """The funding source of the payment method."""

    CREDIT = "credit"
    DEBIT = "debit"
    PREPAID = "prepaid"

    __str__ = str.__str__


FundingSource9OrStr: TypeAlias = Annotated[FundingSource9 | str, open_enum_validator(FundingSource9)]
