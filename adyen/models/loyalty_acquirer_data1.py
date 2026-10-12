from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction_idtype import TransactionIdtype, TransactionIdtypeDict


class LoyaltyAcquirerData1(SdkBaseModel):
    """Data related to the loyalty Acquirer during a loyalty transaction. If content not empty."""

    loyalty_acquirer_id: Optional[str] = Field(default=UNSET, alias="LoyaltyAcquirerID")
    """Identification of the loyalty Acquirer."""

    approval_code: Optional[str] = Field(default=UNSET, alias="ApprovalCode")
    """Code assigned to a transaction approval by the Acquirer. Could be an identifier of the approved transaction for
    the Acquirer. This data element is conditional for the Loyalty Acquirers. Used in the PaymentRequest request for a
    referral."""

    loyalty_transaction_id: Optional[TransactionIdtype] = Field(default=UNSET, alias="LoyaltyTransactionID")
    """Identification of a transaction for the Sale System or the POI System."""

    host_reconciliation_id: Optional[str] = Field(default=UNSET, alias="HostReconciliationID")
    """Identifier of a reconciliation period with a payment or loyalty host. Allows the assignment of a transaction to
    the Acquirer reconciliation (or batch)."""


class LoyaltyAcquirerData1Dict(TypedDict):
    loyalty_acquirer_id: NotRequired[str]
    approval_code: NotRequired[str]
    loyalty_transaction_id: NotRequired[TransactionIdtypeDict]
    host_reconciliation_id: NotRequired[str]
