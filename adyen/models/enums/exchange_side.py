from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ExchangeSide(str, Enum):
    BUY = "buy"
    SELL = "sell"

    __str__ = str.__str__


ExchangeSideOrStr: TypeAlias = Annotated[ExchangeSide | str, open_enum_validator(ExchangeSide)]
