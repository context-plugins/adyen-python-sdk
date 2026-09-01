from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccountHolderType(str, Enum):
    """The account holder type (personal or business)."""

    BUSINESS = "business"
    PERSONAL = "personal"

    __str__ = str.__str__


AccountHolderTypeOrStr: TypeAlias = Annotated[AccountHolderType | str, open_enum_validator(AccountHolderType)]
