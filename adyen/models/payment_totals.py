from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.transaction_type11 import TransactionType11OrStr


class PaymentTotals(SdkBaseModel):
    """Totals of the payment transaction during the reconciliation period."""

    transaction_type: TransactionType11OrStr = Field(alias="TransactionType")
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

    transaction_count: int = Field(alias="TransactionCount")
    """Number of processed transaction during the period."""

    transaction_amount: float = Field(alias="TransactionAmount")
    """Sum of amount of processed transaction during the period."""


class PaymentTotalsDict(TypedDict):
    transaction_type: TransactionType11OrStr
    transaction_count: int
    transaction_amount: float
