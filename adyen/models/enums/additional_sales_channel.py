from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AdditionalSalesChannel(str, Enum):
    E_COMMERCE = "eCommerce"
    ECOM_MOTO = "ecomMoto"
    POS = "pos"
    POS_MOTO = "posMoto"

    __str__ = str.__str__


AdditionalSalesChannelOrStr: TypeAlias = Annotated[
    AdditionalSalesChannel | str, open_enum_validator(AdditionalSalesChannel)
]
