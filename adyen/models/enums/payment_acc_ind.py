from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentAccInd(str, Enum):
    """Indicates the length of time that the payment account was enrolled in the cardholder’s account with the 3DS
    Requestor. Allowed values:
    * **01** — No account (guest checkout)
    * **02** — During this transaction
    * **03** — Less than 30 days
    * **04** — 30–60 days
    * **05** — More than 60 days"""

    _01 = "01"
    _02 = "02"
    _03 = "03"
    _04 = "04"
    _05 = "05"

    __str__ = str.__str__


PaymentAccIndOrStr: TypeAlias = Annotated[PaymentAccInd | str, open_enum_validator(PaymentAccInd)]
