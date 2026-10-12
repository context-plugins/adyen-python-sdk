from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .amount17 import Amount17, Amount17Dict
from .counterparty_v31 import CounterpartyV31, CounterpartyV31Dict
from .direct_debit_information1 import DirectDebitInformation1, DirectDebitInformation1Dict
from .enums.category3 import Category3OrStr
from .enums.direction import DirectionOrStr
from .enums.reason2 import Reason2OrStr
from .enums.status51 import Status51OrStr
from .enums.type83 import Type83OrStr
from .execution_date1 import ExecutionDate1, ExecutionDate1Dict
from .payment_instrument3 import PaymentInstrument3, PaymentInstrument3Dict
from .resource_reference1 import ResourceReference1, ResourceReference1Dict
from .resource_reference5 import ResourceReference5, ResourceReference5Dict
from .transfer_review1 import TransferReview1, TransferReview1Dict
from .ultimate_party_identification1 import UltimatePartyIdentification1, UltimatePartyIdentification1Dict
from .unions.category_data import CategoryData, CategoryDataDict


class Transfer(SdkBaseModel):
    account_holder: Optional[ResourceReference5] = Field(default=UNSET, alias="accountHolder")
    """The account holder associated with the balance account involved in the transfer."""

    amount: Amount17
    """The amount of the transfer."""

    balance_account: Optional[ResourceReference1] = Field(default=UNSET, alias="balanceAccount")
    """Contains information about the balance account involved in the transfer."""

    category: Category3OrStr
    """The category of the transfer.

    Possible values:

     - **bank**: A transfer involving a `transfer instrument
            <https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id>`__ or a
            bank account.

    - **card**: A transfer involving a third-party card.

    - **internal**: A transfer between `balance accounts
        <https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts#responses-200-id>`__ within
        your platform.

    - **issuedCard**: A transfer initiated by an Adyen-issued card.

    - **platformPayment**: Funds movements related to payments that are acquired for your users.

    - **topUp**: An incoming transfer initiated by your user to top up their balance account."""

    category_data: Optional[CategoryData] = Field(default=UNSET, alias="categoryData")
    """The relevant data according to the transfer category."""

    counterparty: CounterpartyV31
    """The other party in the transfer."""

    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    """The date and time when the transfer was created, in ISO 8601 extended format. For example,
    **2020-12-18T10:15:30+01:00**."""

    creation_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="creationDate")
    """The date and time when the event was triggered, in ISO 8601 extended format. For example,
    **2020-12-18T10:15:30+01:00**."""

    description: Optional[str] = UNSET
    """Your description for the transfer. It is used by most banks as the transfer description. We recommend sending a
    maximum of 140 characters, otherwise the description may be truncated.

    Supported characters: **[a-z] [A-Z] [0-9] / - ?** **: ( ) . , ' + Space**

    Supported characters for **regular** and **fast** transfers to a US counterparty: **[a-z] [A-Z] [0-9] & $ % # @**
    **~ = + - _ ' " ! ?**"""

    direct_debit_information: Optional[DirectDebitInformation1] = Field(default=UNSET, alias="directDebitInformation")
    """The details of the direct debit."""

    direction: Optional[DirectionOrStr] = UNSET
    """The direction of the transfer.

    Possible values: **incoming**, **outgoing**."""

    execution_date: Optional[ExecutionDate1] = Field(default=UNSET, alias="executionDate")
    """Contains information about the date when the transfer will be processed. The execution date must be within 30
    days of the current date.

    Until the execution date:
    - The ``status`` of the transfer remains as **received**.
    - The ``reason`` of the transfer remains as **pending**."""

    id: Optional[str] = UNSET
    """The ID of the resource."""

    payment_instrument: Optional[PaymentInstrument3] = Field(default=UNSET, alias="paymentInstrument")
    """Contains information about the payment instrument used in the transfer."""

    reason: Optional[Reason2OrStr] = UNSET
    """Additional information about the status of the transfer."""

    reference: Optional[str] = UNSET
    """Your reference for the transfer, used internally within your platform. If you don't provide this in the request,
    Adyen generates a unique reference."""

    reference_for_beneficiary: Optional[str] = Field(default=UNSET, alias="referenceForBeneficiary")
    """A reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer,
    so you can use it to track statuses for both the source and recipient of funds.

     Supported characters: **a-z**, **A-Z**, **0-9**.The maximum length depends on the ``category``.

     - **internal**: 80 characters

    - **bank**: 35 characters when transferring to an IBAN, 15 characters for others."""

    review: Optional[TransferReview1] = UNSET
    """Contains status updates related to additional reviews."""

    status: Status51OrStr
    """The result of the transfer.

    For example:

    - **received**: an outgoing transfer request is created.
    - **refused**: the transfer request is rejected by Adyen for one of the following reasons:
      - Transfer limit exceeded.
      - Transaction rule requirements violated.
    - **authorised**: the transfer request is authorized and the funds are reserved.
    - **booked**: the funds are deducted from your user's balance account.
     - **failed**: the transfer is rejected by the counterparty's bank.
    - **returned**: the transfer is returned by the counterparty's bank."""

    type_: Optional[Type83OrStr] = Field(default=UNSET, alias="type")
    """The type of transfer or transaction. For example, **refund**, **payment**, **internalTransfer**,
    **bankTransfer**."""

    ultimate_party: Optional[UltimatePartyIdentification1] = Field(default=UNSET, alias="ultimateParty")
    """The ultimate sender of the funds of the transfer (ultimate debtor)."""


class TransferDict(TypedDict):
    account_holder: NotRequired[ResourceReference5Dict]
    amount: Amount17Dict
    balance_account: NotRequired[ResourceReference1Dict]
    category: Category3OrStr
    category_data: NotRequired[CategoryDataDict]
    counterparty: CounterpartyV31Dict
    created_at: NotRequired[RFC3339DateTime]
    creation_date: NotRequired[RFC3339DateTime]
    description: NotRequired[str]
    direct_debit_information: NotRequired[DirectDebitInformation1Dict]
    direction: NotRequired[DirectionOrStr]
    execution_date: NotRequired[ExecutionDate1Dict]
    id: NotRequired[str]
    payment_instrument: NotRequired[PaymentInstrument3Dict]
    reason: NotRequired[Reason2OrStr]
    reference: NotRequired[str]
    reference_for_beneficiary: NotRequired[str]
    review: NotRequired[TransferReview1Dict]
    status: Status51OrStr
    type_: NotRequired[Type83OrStr]
    ultimate_party: NotRequired[UltimatePartyIdentification1Dict]
