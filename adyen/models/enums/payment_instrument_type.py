from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentInstrumentType(str, Enum):
    """The type of the payment instrument. For example, "BankAccount" or "Card"."""

    BANK_ACCOUNT = "BankAccount"
    CARD = "Card"

    __str__ = str.__str__


PaymentInstrumentTypeOrStr: TypeAlias = Annotated[
    PaymentInstrumentType | str, open_enum_validator(PaymentInstrumentType)
]
