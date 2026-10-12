from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .amount17 import Amount17, Amount17Dict
from .balance_mutation import BalanceMutation, BalanceMutationDict
from .direct_debit_information1 import DirectDebitInformation1, DirectDebitInformation1Dict
from .enums.category3 import Category3OrStr
from .enums.direction import DirectionOrStr
from .enums.reason2 import Reason2OrStr
from .enums.status51 import Status51OrStr
from .enums.type83 import Type83OrStr
from .execution_date1 import ExecutionDate1, ExecutionDate1Dict
from .external_reason2 import ExternalReason2, ExternalReason2Dict
from .network_reason2 import NetworkReason2, NetworkReason2Dict
from .payment_instrument3 import PaymentInstrument3, PaymentInstrument3Dict
from .resource_reference1 import ResourceReference1, ResourceReference1Dict
from .resource_reference5 import ResourceReference5, ResourceReference5Dict
from .transaction_rules_result2 import TransactionRulesResult2, TransactionRulesResult2Dict
from .transfer_event import TransferEvent, TransferEventDict
from .transfer_notification_counter_party2 import (
    TransferNotificationCounterParty2,
    TransferNotificationCounterParty2Dict,
)
from .transfer_review1 import TransferReview1, TransferReview1Dict
from .ultimate_party_identification1 import UltimatePartyIdentification1, UltimatePartyIdentification1Dict
from .unions.category_data import CategoryData, CategoryDataDict
from .unions.tracing import Tracing, TracingDict
from .unions.tracking import Tracking, TrackingDict


class TransferData(SdkBaseModel):
    account_holder: Optional[ResourceReference5] = Field(default=UNSET, alias="accountHolder")
    """The account holder associated with the balance account involved in the transfer."""

    amount: Amount17
    """The amount of the transfer."""

    balance_account: Optional[ResourceReference1] = Field(default=UNSET, alias="balanceAccount")
    """Contains information about the balance account involved in the transfer."""

    balance_platform: Optional[str] = Field(default=UNSET, alias="balancePlatform")
    """The unique identifier of the balance platform."""

    balances: Optional[list[BalanceMutation]] = UNSET
    """The list of the latest balance statuses in the transfer."""

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

    counterparty: Optional[TransferNotificationCounterParty2] = UNSET
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

    event_id: Optional[str] = Field(default=UNSET, alias="eventId")
    """The unique identifier of the latest transfer event. Included only when the ``category`` is **issuedCard**."""

    events: Optional[list[TransferEvent]] = UNSET
    """The list of events leading up to the current status of the transfer."""

    execution_date: Optional[ExecutionDate1] = Field(default=UNSET, alias="executionDate")
    """Contains information about the date when the transfer will be processed. The execution date must be within 30
    days of the current date.

    Until the execution date:
    - The ``status`` of the transfer remains as **received**.
    - The ``reason`` of the transfer remains as **pending**."""

    external_reason: Optional[ExternalReason2] = Field(default=UNSET, alias="externalReason")
    """The external reason of this transfer."""

    id: Optional[str] = UNSET
    """The ID of the resource."""

    network_reason: Optional[NetworkReason2] = Field(default=UNSET, alias="networkReason")
    """Contains information that explains why the transfer was rejected or returned by the network."""

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

    sequence_number: Optional[int] = Field(default=UNSET, alias="sequenceNumber")
    """The sequence number of the transfer webhook. The numbers start from 1 and increase with each new webhook for a
    specific transfer.

    The sequence number can help you restore the correct sequence of events even if they arrive out of order."""

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

    tracing: Optional[Tracing] = UNSET
    """Contains information for tracing the transfer after Adyen forwards it to the network."""

    tracking: Optional[Tracking] = UNSET
    """The latest tracking information of the transfer."""

    transaction_rules_result: Optional[TransactionRulesResult2] = Field(default=UNSET, alias="transactionRulesResult")
    """Contains the results of the evaluation of the transaction rules."""

    type_: Optional[Type83OrStr] = Field(default=UNSET, alias="type")
    """The type of transfer or transaction. For example, **refund**, **payment**, **internalTransfer**,
    **bankTransfer**."""

    ultimate_party: Optional[UltimatePartyIdentification1] = Field(default=UNSET, alias="ultimateParty")
    """The ultimate sender of the funds of the transfer (ultimate debtor)."""

    updated_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedAt")
    """The date and time when the event was triggered, in ISO 8601 extended format. For example,
    **2020-12-18T10:15:30+01:00**."""


class TransferDataDict(TypedDict):
    account_holder: NotRequired[ResourceReference5Dict]
    amount: Amount17Dict
    balance_account: NotRequired[ResourceReference1Dict]
    balance_platform: NotRequired[str]
    balances: NotRequired[list[BalanceMutationDict]]
    category: Category3OrStr
    category_data: NotRequired[CategoryDataDict]
    counterparty: NotRequired[TransferNotificationCounterParty2Dict]
    created_at: NotRequired[RFC3339DateTime]
    creation_date: NotRequired[RFC3339DateTime]
    description: NotRequired[str]
    direct_debit_information: NotRequired[DirectDebitInformation1Dict]
    direction: NotRequired[DirectionOrStr]
    event_id: NotRequired[str]
    events: NotRequired[list[TransferEventDict]]
    execution_date: NotRequired[ExecutionDate1Dict]
    external_reason: NotRequired[ExternalReason2Dict]
    id: NotRequired[str]
    network_reason: NotRequired[NetworkReason2Dict]
    payment_instrument: NotRequired[PaymentInstrument3Dict]
    reason: NotRequired[Reason2OrStr]
    reference: NotRequired[str]
    reference_for_beneficiary: NotRequired[str]
    review: NotRequired[TransferReview1Dict]
    sequence_number: NotRequired[int]
    status: Status51OrStr
    tracing: NotRequired[TracingDict]
    tracking: NotRequired[TrackingDict]
    transaction_rules_result: NotRequired[TransactionRulesResult2Dict]
    type_: NotRequired[Type83OrStr]
    ultimate_party: NotRequired[UltimatePartyIdentification1Dict]
    updated_at: NotRequired[RFC3339DateTime]
