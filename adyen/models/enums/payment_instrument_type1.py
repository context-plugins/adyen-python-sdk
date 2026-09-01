from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentInstrumentType1(str, Enum):
    """Possible values:
    * **Card**
    * **Check**
    * **Mobile**
    * **StoredValue**
    * **Cash**"""

    CARD = "Card"
    CHECK = "Check"
    MOBILE = "Mobile"
    STORED_VALUE = "StoredValue"
    CASH = "Cash"

    __str__ = str.__str__


PaymentInstrumentType1OrStr: TypeAlias = Annotated[
    PaymentInstrumentType1 | str, open_enum_validator(PaymentInstrumentType1)
]
