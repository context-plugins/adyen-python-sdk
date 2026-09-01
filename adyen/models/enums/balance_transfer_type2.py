from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BalanceTransferType2(str, Enum):
    """The type of balance transfer. Possible values: **tax**, **fee**, **terminalSale**, **credit**, **debit**, and
    **adjustment**."""

    TAX = "tax"
    FEE = "fee"
    TERMINAL_SALE = "terminalSale"
    CREDIT = "credit"
    DEBIT = "debit"
    ADJUSTMENT = "adjustment"

    __str__ = str.__str__


BalanceTransferType2OrStr: TypeAlias = Annotated[BalanceTransferType2 | str, open_enum_validator(BalanceTransferType2)]
