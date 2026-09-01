from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ExchangeSide2(str, Enum):
    """The operation performed on the source amount. Possible values:
    * **buy**
    * **sell**"""

    BUY = "buy"
    SELL = "sell"

    __str__ = str.__str__


ExchangeSide2OrStr: TypeAlias = Annotated[ExchangeSide2 | str, open_enum_validator(ExchangeSide2)]
