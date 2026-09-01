from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConditionType(str, Enum):
    """Define when you want to get notified about a balance change. Possible values:

    * **greaterThan**: the balance in the account(s) exceeds the specified ``value``.

    * **greaterThanOrEqual**: the balance in the account(s) reaches or exceeds the specified ``value``.

    * **lessThan**: the balance in the account(s) drops below the specified ``value``.

    * **lessThanOrEqual**: the balance in the account(s) reaches to drops below the specified ``value``."""

    GREATER_THAN = "greaterThan"
    GREATER_THAN_OR_EQUAL = "greaterThanOrEqual"
    LESS_THAN = "lessThan"
    LESS_THAN_OR_EQUAL = "lessThanOrEqual"

    __str__ = str.__str__


ConditionTypeOrStr: TypeAlias = Annotated[ConditionType | str, open_enum_validator(ConditionType)]
