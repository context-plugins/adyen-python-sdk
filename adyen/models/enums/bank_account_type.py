from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BankAccountType(str, Enum):
    """The bank account type (checking, savings...)."""

    BALANCE = "balance"
    CHECKING = "checking"
    DEPOSIT = "deposit"
    GENERAL = "general"
    OTHER = "other"
    PAYMENT = "payment"
    SAVINGS = "savings"

    __str__ = str.__str__


BankAccountTypeOrStr: TypeAlias = Annotated[BankAccountType | str, open_enum_validator(BankAccountType)]
