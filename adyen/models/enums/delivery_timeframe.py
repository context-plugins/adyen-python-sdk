from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DeliveryTimeframe(str, Enum):
    """The estimated delivery time for the shopper to receive the goods. Allowed values:
    * ``electronicDelivery``
    * ``sameDayShipping``
    * ``overnightShipping``
    * ``twoOrMoreDaysShipping``"""

    ELECTRONIC_DELIVERY = "electronicDelivery"
    SAME_DAY_SHIPPING = "sameDayShipping"
    OVERNIGHT_SHIPPING = "overnightShipping"
    TWO_OR_MORE_DAYS_SHIPPING = "twoOrMoreDaysShipping"

    __str__ = str.__str__


DeliveryTimeframeOrStr: TypeAlias = Annotated[DeliveryTimeframe | str, open_enum_validator(DeliveryTimeframe)]
