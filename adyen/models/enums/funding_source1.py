from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FundingSource1(str, Enum):
    """The funding source of the payment method.

    Possible values:
    * **credit**
    * **debit**
    * **prepaid**
    * **deferred_debit**
    * **charged**
    * **ANY**"""

    CHARGED = "charged"
    CREDIT = "credit"
    DEBIT = "debit"
    DEFERRED_DEBIT = "deferred_debit"
    PREPAID = "prepaid"
    ANY = "ANY"

    __str__ = str.__str__


FundingSource1OrStr: TypeAlias = Annotated[FundingSource1 | str, open_enum_validator(FundingSource1)]
