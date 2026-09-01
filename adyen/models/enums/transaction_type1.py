from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransactionType1(str, Enum):
    """Possible values:
    * **Debit**
    * **Credit**
    * **ReverseDebit**
    * **ReverseCredit**
    * **OneTimeReservation**
    * **CompletedDeffered**
    * **FirstReservation**
    * **UpdateReservation**
    * **CompletedReservation**
    * **CashAdvance**
    * **IssuerInstalment**
    * **Declined**
    * **Failed**
    * **Award**
    * **ReverseAward**
    * **Redemption**
    * **ReverseRedemption**
    * **Rebate**
    * **ReverseRebate**"""

    DEBIT = "Debit"
    CREDIT = "Credit"
    REVERSE_DEBIT = "ReverseDebit"
    REVERSE_CREDIT = "ReverseCredit"
    ONE_TIME_RESERVATION = "OneTimeReservation"
    COMPLETED_DEFFERED = "CompletedDeffered"
    FIRST_RESERVATION = "FirstReservation"
    UPDATE_RESERVATION = "UpdateReservation"
    COMPLETED_RESERVATION = "CompletedReservation"
    CASH_ADVANCE = "CashAdvance"
    ISSUER_INSTALMENT = "IssuerInstalment"
    DECLINED = "Declined"
    FAILED = "Failed"
    AWARD = "Award"
    REVERSE_AWARD = "ReverseAward"
    REDEMPTION = "Redemption"
    REVERSE_REDEMPTION = "ReverseRedemption"
    REBATE = "Rebate"
    REVERSE_REBATE = "ReverseRebate"

    __str__ = str.__str__


TransactionType1OrStr: TypeAlias = Annotated[TransactionType1 | str, open_enum_validator(TransactionType1)]
