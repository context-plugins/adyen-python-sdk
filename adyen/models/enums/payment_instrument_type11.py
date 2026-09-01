from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentInstrumentType11(str, Enum):
    """Type of payment instrument. Possible values:
    * **Card**
    * **Cash**
    * **Check**
    * **Mobile**
    * **StoredValue**"""

    CARD = "Card"
    CHECK = "Check"
    MOBILE = "Mobile"
    STORED_VALUE = "StoredValue"
    CASH = "Cash"

    __str__ = str.__str__


PaymentInstrumentType11OrStr: TypeAlias = Annotated[
    PaymentInstrumentType11 | str, open_enum_validator(PaymentInstrumentType11)
]
