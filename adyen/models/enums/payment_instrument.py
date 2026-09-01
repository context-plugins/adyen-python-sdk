from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentInstrument(str, Enum):
    """Sets the allowed payment instrument for Pay at table transactions. Can be: **cash** or **card**. If not set, the
    terminal presents both options."""

    CASH = "Cash"
    CARD = "Card"

    __str__ = str.__str__


PaymentInstrumentOrStr: TypeAlias = Annotated[PaymentInstrument | str, open_enum_validator(PaymentInstrument)]
