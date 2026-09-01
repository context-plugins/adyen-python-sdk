from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AmountRule(str, Enum):
    """The limitation rule of the billing amount.

    Possible values:
     * **max**: The transaction amount can not exceed the ``amount``.

     * **exact**: The transaction amount should be the same as the ``amount``."""

    MAX = "max"
    EXACT = "exact"

    __str__ = str.__str__


AmountRuleOrStr: TypeAlias = Annotated[AmountRule | str, open_enum_validator(AmountRule)]
