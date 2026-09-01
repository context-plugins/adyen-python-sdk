from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccountType11(str, Enum):
    """The type of the bank account. Possible values are **CURRENT**, **SAVINGS**, **BUSINESS**, **CREDIT_CARD**,
    **LOAN**, **UNKNOWN**."""

    CURRENT = "CURRENT"
    SAVINGS = "SAVINGS"
    BUSINESS = "BUSINESS"
    CREDIT_CARD = "CREDIT_CARD"
    LOAN = "LOAN"
    UNKNOWN = "UNKNOWN"

    __str__ = str.__str__


AccountType11OrStr: TypeAlias = Annotated[AccountType11 | str, open_enum_validator(AccountType11)]
