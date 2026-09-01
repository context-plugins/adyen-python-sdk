from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction_idtype6 import TransactionIdtype6, TransactionIdtype6Dict


class PaymentAcquirerData(SdkBaseModel):
    """Data related to the response from the payment Acquirer."""

    acquirer_id: Optional[int] = Field(default=UNSET, alias="AcquirerID")
    """Identification of the Acquirer. Identification of the Acquirer when the POI System is multi-acquirer."""

    merchant_id: str = Field(alias="MerchantID")
    """Identification of the Merchant for the Acquirer."""

    acquirer_poiid: str = Field(alias="AcquirerPOIID")
    """Identification of the POI for the payment Acquirer."""

    acquirer_transaction_id: Optional[TransactionIdtype6] = Field(default=UNSET, alias="AcquirerTransactionID")
    """Identification of the Transaction for the Acquirer. If provided by the Acquirer."""

    approval_code: Optional[str] = Field(default=UNSET, alias="ApprovalCode")
    """Code assigned to a transaction approval by the Acquirer. If available."""

    host_reconciliation_id: Optional[str] = Field(default=UNSET, alias="HostReconciliationID")
    """Identifier of a reconciliation period with a payment or loyalty host. Allows the assignment of a transaction to
    the Acquirer reconciliation (or batch)."""


class PaymentAcquirerDataDict(TypedDict):
    acquirer_id: NotRequired[int]
    merchant_id: str
    acquirer_poiid: str
    acquirer_transaction_id: NotRequired[TransactionIdtype6 | TransactionIdtype6Dict]
    approval_code: NotRequired[str]
    host_reconciliation_id: NotRequired[str]
