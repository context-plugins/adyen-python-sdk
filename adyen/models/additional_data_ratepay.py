from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdditionalDataRatepay(SdkBaseModel):
    ratepay_installment_amount: Optional[str] = Field(default=UNSET, alias="ratepay.installmentAmount")
    """Amount the customer has to pay each month."""

    ratepay_interest_rate: Optional[str] = Field(default=UNSET, alias="ratepay.interestRate")
    """Interest rate of this installment."""

    ratepay_last_installment_amount: Optional[str] = Field(default=UNSET, alias="ratepay.lastInstallmentAmount")
    """Amount of the last installment."""

    ratepay_payment_firstday: Optional[str] = Field(default=UNSET, alias="ratepay.paymentFirstday")
    """Calendar day of the first payment."""

    ratepaydata_delivery_date: Optional[str] = Field(default=UNSET, alias="ratepaydata.deliveryDate")
    """Date the merchant delivered the goods to the customer."""

    ratepaydata_due_date: Optional[str] = Field(default=UNSET, alias="ratepaydata.dueDate")
    """Date by which the customer must settle the payment."""

    ratepaydata_invoice_date: Optional[str] = Field(default=UNSET, alias="ratepaydata.invoiceDate")
    """Invoice date, defined by the merchant. If not included, the invoice date is set to the delivery date."""

    ratepaydata_invoice_id: Optional[str] = Field(default=UNSET, alias="ratepaydata.invoiceId")
    """Identification name or number for the invoice, defined by the merchant."""


class AdditionalDataRatepayDict(TypedDict):
    ratepay_installment_amount: NotRequired[str]
    ratepay_interest_rate: NotRequired[str]
    ratepay_last_installment_amount: NotRequired[str]
    ratepay_payment_firstday: NotRequired[str]
    ratepaydata_delivery_date: NotRequired[str]
    ratepaydata_due_date: NotRequired[str]
    ratepaydata_invoice_date: NotRequired[str]
    ratepaydata_invoice_id: NotRequired[str]
