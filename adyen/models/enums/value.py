from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Value(str, Enum):
    BALANCE_ACCOUNT = "balanceAccount"
    BANK_ACCOUNT = "bankAccount"
    CARD = "card"
    TRANSFER_INSTRUMENT = "transferInstrument"

    __str__ = str.__str__


ValueOrStr: TypeAlias = Annotated[Value | str, open_enum_validator(Value)]
