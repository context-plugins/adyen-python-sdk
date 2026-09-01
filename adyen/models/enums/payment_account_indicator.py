from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentAccountIndicator(str, Enum):
    """Indicator for the length of time since this payment method was added to this shopper's account. Allowed values:
    * notApplicable
    * thisTransaction
    * lessThan30Days
    * from30To60Days
    * moreThan60Days"""

    NOT_APPLICABLE = "notApplicable"
    THIS_TRANSACTION = "thisTransaction"
    LESS_THAN30_DAYS = "lessThan30Days"
    FROM30_TO60_DAYS = "from30To60Days"
    MORE_THAN60_DAYS = "moreThan60Days"

    __str__ = str.__str__


PaymentAccountIndicatorOrStr: TypeAlias = Annotated[
    PaymentAccountIndicator | str, open_enum_validator(PaymentAccountIndicator)
]
