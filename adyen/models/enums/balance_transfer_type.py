from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BalanceTransferType(str, Enum):
    TAX = "tax"
    FEE = "fee"
    TERMINAL_SALE = "terminalSale"
    CREDIT = "credit"
    DEBIT = "debit"
    ADJUSTMENT = "adjustment"

    __str__ = str.__str__


BalanceTransferTypeOrStr: TypeAlias = Annotated[BalanceTransferType | str, open_enum_validator(BalanceTransferType)]
