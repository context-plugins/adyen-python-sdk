from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DeliveryAddressIndicator(str, Enum):
    """Indicator regarding the delivery address. Allowed values:
    * ``shipToBillingAddress``
    * ``shipToVerifiedAddress``
    * ``shipToNewAddress``
    * ``shipToStore``
    * ``digitalGoods``
    * ``goodsNotShipped``
    * ``other``"""

    SHIP_TO_BILLING_ADDRESS = "shipToBillingAddress"
    SHIP_TO_VERIFIED_ADDRESS = "shipToVerifiedAddress"
    SHIP_TO_NEW_ADDRESS = "shipToNewAddress"
    SHIP_TO_STORE = "shipToStore"
    DIGITAL_GOODS = "digitalGoods"
    GOODS_NOT_SHIPPED = "goodsNotShipped"
    OTHER = "other"

    __str__ = str.__str__


DeliveryAddressIndicatorOrStr: TypeAlias = Annotated[
    DeliveryAddressIndicator | str, open_enum_validator(DeliveryAddressIndicator)
]
