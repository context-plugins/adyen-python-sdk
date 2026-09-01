from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Value3(str, Enum):
    ACQUIRER_ID = "acquirerId"
    AMOUNT = "amount"
    CURRENCY = "currency"
    MERCHANT_ID = "merchantId"
    MERCHANT_NAME = "merchantName"

    __str__ = str.__str__


Value3OrStr: TypeAlias = Annotated[Value3 | str, open_enum_validator(Value3)]
