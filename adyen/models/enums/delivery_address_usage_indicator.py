from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DeliveryAddressUsageIndicator(str, Enum):
    """Indicator for the length of time since this delivery address was first used. Allowed values:
    * thisTransaction
    * lessThan30Days
    * from30To60Days
    * moreThan60Days"""

    THIS_TRANSACTION = "thisTransaction"
    LESS_THAN30_DAYS = "lessThan30Days"
    FROM30_TO60_DAYS = "from30To60Days"
    MORE_THAN60_DAYS = "moreThan60Days"

    __str__ = str.__str__


DeliveryAddressUsageIndicatorOrStr: TypeAlias = Annotated[
    DeliveryAddressUsageIndicator | str, open_enum_validator(DeliveryAddressUsageIndicator)
]
