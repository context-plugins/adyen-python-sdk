from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccountType3(str, Enum):
    CURRENT = "CURRENT"
    SAVINGS = "SAVINGS"
    BUSINESS = "BUSINESS"
    CREDIT_CARD = "CREDIT_CARD"
    LOAN = "LOAN"
    UNKNOWN = "UNKNOWN"

    __str__ = str.__str__


AccountType3OrStr: TypeAlias = Annotated[AccountType3 | str, open_enum_validator(AccountType3)]
