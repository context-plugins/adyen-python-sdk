from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccountType2(str, Enum):
    """The bank account type.

    Possible values: **checking** or **savings**. Defaults to **checking**."""

    CHECKING = "checking"
    SAVINGS = "savings"

    __str__ = str.__str__


AccountType2OrStr: TypeAlias = Annotated[AccountType2 | str, open_enum_validator(AccountType2)]
