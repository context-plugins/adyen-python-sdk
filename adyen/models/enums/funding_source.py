from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FundingSource(str, Enum):
    """The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default
    the funding source is credit. To use debit, set this value to **debit**."""

    CREDIT = "credit"
    DEBIT = "debit"
    PREPAID = "prepaid"

    __str__ = str.__str__


FundingSourceOrStr: TypeAlias = Annotated[FundingSource | str, open_enum_validator(FundingSource)]
