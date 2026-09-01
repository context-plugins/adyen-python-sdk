from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransactionType11(str, Enum):
    """Type of transaction for which totals are grouped. Debit, Credit, ReverseDebit, ReverseCredit, OneTimeReservation,
    CompletedDeffered, FirstReservation, UpdateReservation, CompletedReservation, CashAdvance. Possible values:
    * **Award**
    * **CashAdvance**
    * **CompletedDeffered**
    * **CompletedReservation**
    * **Credit**
    * **Debit**
    * **Declined**
    * **Failed**
    * **FirstReservation**
    * **IssuerInstalment**
    * **OneTimeReservation**
    * **Rebate**
    * **Redemption**
    * **ReverseAward**
    * **ReverseCredit**
    * **ReverseDebit**
    * **ReverseRebate**
    * **ReverseRedemption**
    * **UpdateReservation**"""

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


TransactionType11OrStr: TypeAlias = Annotated[TransactionType11 | str, open_enum_validator(TransactionType11)]
