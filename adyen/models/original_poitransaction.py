from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction_idtype4 import TransactionIdtype4, TransactionIdtype4Dict
from .transaction_idtype5 import TransactionIdtype5, TransactionIdtype5Dict


class OriginalPoitransaction(SdkBaseModel):
    """Identification of a previous POI transaction. In the Payment Request message, it allows using the card of a
    previous CardAcquisition or Payment request."""

    sale_id: Optional[str] = Field(default=UNSET, alias="SaleID")
    """Identification of a Sale System for the NEXO SaletoPOI protocol."""

    poiid: Optional[str] = Field(default=UNSET, alias="POIID")
    """Identification of a payment terminal for the NEXO SaletoPOI protocol. If original transaction is coming from
    another POI."""

    poi_transaction_id: Optional[TransactionIdtype4] = Field(default=UNSET, alias="POITransactionID")
    """Unique identification of a POI transaction for a POI. Absent if SaleReferenceID is sufficient to identify the
    transaction."""

    reuse_card_data_flag: bool = Field(default=True, alias="ReuseCardDataFlag")
    """Indicates if the card data has to be retrieved from a previous transaction."""

    approval_code: Optional[str] = Field(default=UNSET, alias="ApprovalCode")
    """Code assigned to a transaction approval by the Acquirer. If referral."""

    acquirer_id: Optional[int] = Field(default=UNSET, alias="AcquirerID")
    """Identification of the Acquirer. Restrict to the Acquirer if present."""

    amount_value: Optional[float] = Field(default=UNSET, alias="AmountValue")
    """Value of an amount."""

    host_transaction_id: Optional[TransactionIdtype5] = Field(default=UNSET, alias="HostTransactionID")
    """Identification of the transaction by the host in charge of the stored value transaction. If POITransactionID not
    present."""


class OriginalPoitransactionDict(TypedDict):
    sale_id: NotRequired[str]
    poiid: NotRequired[str]
    poi_transaction_id: NotRequired[TransactionIdtype4Dict]
    reuse_card_data_flag: NotRequired[bool]
    approval_code: NotRequired[str]
    acquirer_id: NotRequired[int]
    amount_value: NotRequired[float]
    host_transaction_id: NotRequired[TransactionIdtype5Dict]
