from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.payment_instrument_type11 import PaymentInstrumentType11OrStr
from .payment_totals import PaymentTotals, PaymentTotalsDict


class TransactionTotals(SdkBaseModel):
    """If Result is Success, contains all the totals, classified as required by the Sale in the message request. At
    least, transaction totals are provided per Acquirer, Acquirer Settlement, and Card Brand. Result of the Sale to POI
    Reconciliation processing."""

    payment_instrument_type: PaymentInstrumentType11OrStr = Field(alias="PaymentInstrumentType")
    """Type of payment instrument. Possible values:
    * **Card**
    * **Cash**
    * **Check**
    * **Mobile**
    * **StoredValue**"""

    acquirer_id: Optional[int] = Field(default=UNSET, alias="AcquirerID")
    """Identification of the Acquirer."""

    host_reconciliation_id: Optional[str] = Field(default=UNSET, alias="HostReconciliationID")
    """Identifier of a reconciliation period with a payment or loyalty host."""

    card_brand: Optional[str] = Field(default=UNSET, alias="CardBrand")
    """Type of payment or loyalty card. If configured to present totals per card brand, and Response.Result is
    Success."""

    poiid: Optional[str] = Field(default=UNSET, alias="POIID")
    """Identification of a POI System or a POI Terminal for the Sale to POI protocol. Sent if requested in the message
    request."""

    sale_id: Optional[str] = Field(default=UNSET, alias="SaleID")
    """Identification of a Sale System or a Sale Terminal for the Sale to POI protocol. Sent if requested in the message
    request."""

    operator_id: Optional[str] = Field(default=UNSET, alias="OperatorID")
    """Identification of the Cashier or Operator. Sent if requested in the message request."""

    shift_number: Optional[str] = Field(default=UNSET, alias="ShiftNumber")
    """Shift number. Sent if requested in the message request."""

    totals_group_id: Optional[str] = Field(default=UNSET, alias="TotalsGroupID")
    """Identification of a group of transaction on a POI Terminal, having the same Sale features. Sent if requested in
    the message request."""

    payment_currency: Optional[str] = Field(default=UNSET, alias="PaymentCurrency")
    """Currency of a monetary amount."""

    payment_totals: Optional[list[PaymentTotals]] = Field(default=UNSET, alias="PaymentTotals")
    """Totals of the payment transaction during the reconciliation period. If both ``TransactionCount`` and
    ``TransactionAmount`` are not equal to zero."""


class TransactionTotalsDict(TypedDict):
    payment_instrument_type: PaymentInstrumentType11OrStr
    acquirer_id: NotRequired[int]
    host_reconciliation_id: NotRequired[str]
    card_brand: NotRequired[str]
    poiid: NotRequired[str]
    sale_id: NotRequired[str]
    operator_id: NotRequired[str]
    shift_number: NotRequired[str]
    totals_group_id: NotRequired[str]
    payment_currency: NotRequired[str]
    payment_totals: NotRequired[list[PaymentTotalsDict]]
