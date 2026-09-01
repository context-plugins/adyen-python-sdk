from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ShopperInteraction11(str, Enum):
    """The sales channel condition that defines whether the split logic applies.

    Possible values:
    * **Ecommerce**: Online transactions where the cardholder is present.
    * **ContAuth**: Card on file and/or subscription transactions, where the cardholder is known to the merchant
        (returning customer).
    * **Moto**: Mail-order and telephone-order transactions where the customer is in contact with the merchant via email
        or telephone.
    * **POS**: Point-of-sale transactions where the customer is physically present to make a payment using a secure
        payment terminal.
    * **ANY**: All sales channels."""

    ECOMMERCE = "Ecommerce"
    CONT_AUTH = "ContAuth"
    MOTO = "Moto"
    POS = "POS"
    ANY = "ANY"

    __str__ = str.__str__


ShopperInteraction11OrStr: TypeAlias = Annotated[ShopperInteraction11 | str, open_enum_validator(ShopperInteraction11)]
