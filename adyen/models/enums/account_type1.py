from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccountType1(str, Enum):
    """The type of the bank account."""

    BALANCE = "balance"
    CHECKING = "checking"
    DEPOSIT = "deposit"
    GENERAL = "general"
    OTHER = "other"
    PAYMENT = "payment"
    SAVINGS = "savings"

    __str__ = str.__str__


AccountType1OrStr: TypeAlias = Annotated[AccountType1 | str, open_enum_validator(AccountType1)]
