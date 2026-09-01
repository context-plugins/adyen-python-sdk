from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BillingAttemptsRule(str, Enum):
    """The rule to specify the period, within which the recurring debit can happen, relative to the mandate recurring
    date.

    Possible values:

     * **on**: On a specific date.

     * **before**: Before and on a specific date.

     * **after**: On and after a specific date."""

    ON = "on"
    BEFORE = "before"
    AFTER = "after"

    __str__ = str.__str__


BillingAttemptsRuleOrStr: TypeAlias = Annotated[BillingAttemptsRule | str, open_enum_validator(BillingAttemptsRule)]
