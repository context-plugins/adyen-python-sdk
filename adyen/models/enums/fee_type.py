from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FeeType(str, Enum):
    """**Alma payment request fee type**"""

    MERCHANT_PAYS = "merchantPays"
    SHOPPER_PAYS = "shopperPays"

    __str__ = str.__str__


FeeTypeOrStr: TypeAlias = Annotated[FeeType | str, open_enum_validator(FeeType)]
