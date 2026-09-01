from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type181(str, Enum):
    """The resource for which you want to receive notifications. Possible values:

    * **balancePlatform**: receive notifications about balance changes in your entire balance platform.

    * **accountHolder**: receive notifications about balance changes of a specific user.

    * **balanceAccount**: receive notifications about balance changes in a specific balance account."""

    BALANCE_ACCOUNT = "balanceAccount"
    ACCOUNT_HOLDER = "accountHolder"
    BALANCE_PLATFORM = "balancePlatform"

    __str__ = str.__str__


Type181OrStr: TypeAlias = Annotated[Type181 | str, open_enum_validator(Type181)]
