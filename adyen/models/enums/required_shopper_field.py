from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RequiredShopperField(str, Enum):
    BILLING_ADDRESS = "billingAddress"
    DELIVERY_ADDRESS = "deliveryAddress"
    SHOPPER_EMAIL = "shopperEmail"
    SHOPPER_NAME = "shopperName"
    TELEPHONE_NUMBER = "telephoneNumber"

    __str__ = str.__str__


RequiredShopperFieldOrStr: TypeAlias = Annotated[RequiredShopperField | str, open_enum_validator(RequiredShopperField)]
