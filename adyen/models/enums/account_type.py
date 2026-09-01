from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccountType(str, Enum):
    """Indicates the type of account. For example, for a multi-account card product. Allowed values:
    * notApplicable
    * credit
    * debit"""

    NOT_APPLICABLE = "notApplicable"
    CREDIT = "credit"
    DEBIT = "debit"

    __str__ = str.__str__


AccountTypeOrStr: TypeAlias = Annotated[AccountType | str, open_enum_validator(AccountType)]
