from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Value4(str, Enum):
    ATM_WITHDRAW = "atmWithdraw"
    BALANCE_INQUIRY = "balanceInquiry"
    ECOMMERCE = "ecommerce"
    MOTO = "moto"
    POS = "pos"
    RECURRING = "recurring"
    TOKEN = "token"
    UNKNOWN = "unknown"

    __str__ = str.__str__


Value4OrStr: TypeAlias = Annotated[Value4 | str, open_enum_validator(Value4)]
