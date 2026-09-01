from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentType(str, Enum):
    """Possible values:
    * **Normal**
    * **Refund**
    * **OneTimeReservation**
    * **FirstReservation**
    * **UpdateReservation**
    * **Completion**
    * **CashAdvance**
    * **CashDeposit**
    * **Recurring**
    * **Instalment**
    * **IssuerInstalment**
    * **PaidOut**"""

    NORMAL = "Normal"
    REFUND = "Refund"
    ONE_TIME_RESERVATION = "OneTimeReservation"
    FIRST_RESERVATION = "FirstReservation"
    UPDATE_RESERVATION = "UpdateReservation"
    COMPLETION = "Completion"
    CASH_ADVANCE = "CashAdvance"
    CASH_DEPOSIT = "CashDeposit"
    RECURRING = "Recurring"
    INSTALMENT = "Instalment"
    ISSUER_INSTALMENT = "IssuerInstalment"
    PAID_OUT = "PaidOut"

    __str__ = str.__str__


PaymentTypeOrStr: TypeAlias = Annotated[PaymentType | str, open_enum_validator(PaymentType)]
