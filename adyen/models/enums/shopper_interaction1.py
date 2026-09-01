from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ShopperInteraction1(str, Enum):
    """The sales channel. Required if:
    - The merchant account does not have a sales channel.
    - ``type`` is **alipay**.

    When you provide this field, it overrides the default sales channel set on the merchant account.

    Possible values: **eCommerce**, **pos**, **contAuth**, and **moto**."""

    E_COMMERCE = "eCommerce"
    POS = "pos"
    MOTO = "moto"
    CONT_AUTH = "contAuth"

    __str__ = str.__str__


ShopperInteraction1OrStr: TypeAlias = Annotated[ShopperInteraction1 | str, open_enum_validator(ShopperInteraction1)]
