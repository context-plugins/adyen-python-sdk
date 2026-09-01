from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccountChangeIndicator(str, Enum):
    """Indicator for the length of time since the shopper's account was last updated. Allowed values:
    * thisTransaction
    * lessThan30Days
    * from30To60Days
    * moreThan60Days, Indicator for the length of time since this delivery address was first used.
    Allowed values:
    * thisTransaction
    * lessThan30Days
    * from30To60Days
    * moreThan60Days"""

    THIS_TRANSACTION = "thisTransaction"
    LESS_THAN30_DAYS = "lessThan30Days"
    FROM30_TO60_DAYS = "from30To60Days"
    MORE_THAN60_DAYS = "moreThan60Days"

    __str__ = str.__str__


AccountChangeIndicatorOrStr: TypeAlias = Annotated[
    AccountChangeIndicator | str, open_enum_validator(AccountChangeIndicator)
]
