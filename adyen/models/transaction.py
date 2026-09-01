from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .amount17 import Amount17, Amount17Dict
from .enums.status72 import Status72OrStr
from .payment_instrument21 import PaymentInstrument21, PaymentInstrument21Dict
from .resource_reference3 import ResourceReference3, ResourceReference3Dict
from .resource_reference4 import ResourceReference4, ResourceReference4Dict
from .transfer_view2 import TransferView2, TransferView2Dict


class Transaction(SdkBaseModel):
    account_holder: ResourceReference3 = Field(alias="accountHolder")
    """Contains information about the account holder associated with the ``balanceAccount``."""

    amount: Amount17
    """Contains information about the amount of the transaction."""

    balance_account: ResourceReference4 = Field(alias="balanceAccount")
    """Contains information about the balance account involved in the transaction."""

    balance_platform: str = Field(alias="balancePlatform")
    """The unique identifier of the balance platform."""

    booking_date: RFC3339DateTime = Field(alias="bookingDate")
    """The date the transaction was booked into the balance account."""

    creation_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="creationDate")
    """The date and time when the event was triggered, in ISO 8601 extended format. For example,
    **2025-03-19T10:15:30+01:00**."""

    description: Optional[str] = UNSET
    """The ``description`` from the ``/transfers`` request."""

    id: str
    """The unique identifier of the transaction."""

    payment_instrument: Optional[PaymentInstrument21] = Field(default=UNSET, alias="paymentInstrument")
    """Contains information about the payment instrument that was used for the transaction."""

    reference_for_beneficiary: Optional[str] = Field(default=UNSET, alias="referenceForBeneficiary")
    """The reference sent to or received from the counterparty.

    * For outgoing funds, this is the
        https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__resParam_referenceForBeneficiary from the
        https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__reqParam_referenceForBeneficiary request.

     * For incoming funds, this is the reference from the sender."""

    status: Status72OrStr
    """The status of the transaction.

     Possible values:

    * **pending**: The transaction is still pending.

    * **booked**: The transaction has been booked to the balance account."""

    transfer: Optional[TransferView2] = UNSET
    """Contains information about the transfer related to the transaction."""

    value_date: RFC3339DateTime = Field(alias="valueDate")
    """The date the transfer amount becomes available in the balance account."""


class TransactionDict(TypedDict):
    account_holder: ResourceReference3 | ResourceReference3Dict
    amount: Amount17 | Amount17Dict
    balance_account: ResourceReference4 | ResourceReference4Dict
    balance_platform: str
    booking_date: RFC3339DateTime
    creation_date: NotRequired[RFC3339DateTime]
    description: NotRequired[str]
    id: str
    payment_instrument: NotRequired[PaymentInstrument21 | PaymentInstrument21Dict]
    reference_for_beneficiary: NotRequired[str]
    status: Status72OrStr
    transfer: NotRequired[TransferView2 | TransferView2Dict]
    value_date: RFC3339DateTime
