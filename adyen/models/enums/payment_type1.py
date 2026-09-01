from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentType1(str, Enum):
    """Type of payment transaction. Elements requested by the Sale System that are related to the payment only. Possible
    values:
    * **CashAdvance**
    * **CashDeposit**
    * **Completion**
    * **FirstReservation**
    * **Instalment**
    * **IssuerInstalment**
    * **Normal**
    * **OneTimeReservation**
    * **PaidOut**
    * **Recurring**
    * **Refund**
    * **UpdateReservation**"""

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


PaymentType1OrStr: TypeAlias = Annotated[PaymentType1 | str, open_enum_validator(PaymentType1)]
