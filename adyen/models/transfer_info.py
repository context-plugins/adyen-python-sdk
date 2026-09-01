from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount17 import Amount17, Amount17Dict
from .counterparty_info_v31 import CounterpartyInfoV31, CounterpartyInfoV31Dict
from .enums.category3 import Category3OrStr
from .enums.priority1 import Priority1OrStr
from .enums.type113 import Type113OrStr
from .execution_date3 import ExecutionDate3, ExecutionDate3Dict
from .transfer_request_review2 import TransferRequestReview2, TransferRequestReview2Dict
from .ultimate_party_identification1 import UltimatePartyIdentification1, UltimatePartyIdentification1Dict


class TransferInfo(SdkBaseModel):
    amount: Amount17
    """The amount of the transfer."""

    balance_account_id: Optional[str] = Field(default=UNSET, alias="balanceAccountId")
    """The unique identifier of the source `balance account
    <https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts#responses-200-id>`__.

    If you want to make a transfer using a **virtual** **bankAccount** assigned to the balance account, you must specify
    the `payment instrument ID
    <https://docs.adyen.com/api-explorer/balanceplatform/latest/post/paymentInstruments#responses-200-id>`__ of the
    **virtual** **bankAccount**. If you only specify a balance account ID, Adyen uses the default **physical**
    **bankAccount** payment instrument assigned to the balance account."""

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

    counterparty: CounterpartyInfoV31
    """The other party involved in the funds transfer. A bank account, a balance account, a card, or a transfer
    instrument is required."""

    description: Optional[str] = UNSET
    """Your description for the transfer. It is used by most banks as the transfer description. We recommend sending a
    maximum of 140 characters, otherwise the description may be truncated.

    Supported characters: **[a-z] [A-Z] [0-9] / - ?** **: ( ) . , ' + Space**

    Supported characters for **regular** and **fast** transfers to a US counterparty: **[a-z] [A-Z] [0-9] & $ % # @**
    **~ = + - _ ' " ! ?**"""

    execution_date: Optional[ExecutionDate3] = Field(default=UNSET, alias="executionDate")
    """The date when the transfer will be processed. This date must be within 30 days of the current date.

    Until the ``executionDate``:
    - The ``status`` of the transfer remains as **received**.
    - The ``reason`` of the transfer remains as **pending**."""

    payment_instrument_id: Optional[str] = Field(default=UNSET, alias="paymentInstrumentId")
    """The unique identifier of the source `payment instrument
    <https://docs.adyen.com/api-explorer/balanceplatform/latest/post/paymentInstruments#responses-200-id>`__.

    If you want to make a transfer using a **virtual** **bankAccount**, you must specify the payment instrument ID of
    the **virtual** **bankAccount**. If you only specify a balance account ID, Adyen uses the default **physical**
    **bankAccount** payment instrument assigned to the balance account."""

    priorities: Optional[list[Priority1OrStr]] = UNSET
    """The list of priorities for the bank transfer. This sets the speed at which the transfer is sent and the fees that
    you have to pay. You can provide multiple priorities. Adyen will try to pay out using the priority you list first.
    If that's not possible, it moves on to the next option in the order of your provided priorities.

    Possible values:

    * **regular**: For normal, low-value transactions.

    * **fast**: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value
        transactions.

    * **wire**: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority,
        high-value transactions.

    * **instant**: For instant funds transfers within the United States and in `SEPA locations
        <https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html>`__.

    * **crossBorder**: For high-value transfers to a recipient in a different country.

    * **internal**: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).

    Required for transfers with ``category`` **bank**. For more details, see `fallback priorities
    <https://docs.adyen.com/payouts/payout-service/payout-to-users/#fallback-priorities>`__."""

    priority: Optional[Priority1OrStr] = UNSET
    """The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have
    to pay. Required for transfers with ``category`` **bank**.

    Possible values:

    * **regular**: For normal, low-value transactions.

    * **fast**: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value
        transactions.

    * **wire**: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority,
        high-value transactions.

    * **instant**: For instant funds transfers within the United States and in `SEPA locations
        <https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html>`__.

    * **crossBorder**: For high-value transfers to a recipient in a different country.

    * **internal**: For transfers to an Adyen-issued business bank account (by bank account number/IBAN)."""

    reference: Optional[str] = UNSET
    """Your reference for the transfer, used internally within your platform. If you don't provide this in the request,
    Adyen generates a unique reference."""

    reference_for_beneficiary: Optional[str] = Field(default=UNSET, alias="referenceForBeneficiary")
    """A reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer,
    so you can use it to track statuses for both parties involved in the funds movement.

     Supported characters: **a-z**, **A-Z**, **0-9**. The maximum length depends on the ``category``.

    - **internal**: 80 characters

    - **bank**: 35 characters when transferring to an IBAN, 15 characters for others."""

    review: Optional[TransferRequestReview2] = UNSET
    """Contains information required for triggering transfer reviews."""

    type_: Optional[Type113OrStr] = Field(default=UNSET, alias="type")
    """The type of transfer.

    Possible values:

     - **bankTransfer**: for push transfers to a transfer instrument or a bank account. The ``category`` must be
            **bank**.
    - **internalTransfer**: for push transfers between balance accounts. The ``category`` must be **internal**.
    - **internalDirectDebit**: for pull transfers (direct debits) between balance accounts. The ``category`` must be
        **internal**."""

    ultimate_party: Optional[UltimatePartyIdentification1] = Field(default=UNSET, alias="ultimateParty")
    """The ultimate sender of the funds of the transfer (ultimate debtor)."""


class TransferInfoDict(TypedDict):
    amount: Amount17 | Amount17Dict
    balance_account_id: NotRequired[str]
    category: Category3OrStr
    counterparty: CounterpartyInfoV31 | CounterpartyInfoV31Dict
    description: NotRequired[str]
    execution_date: NotRequired[ExecutionDate3 | ExecutionDate3Dict]
    payment_instrument_id: NotRequired[str]
    priorities: NotRequired[list[Priority1OrStr]]
    priority: NotRequired[Priority1OrStr]
    reference: NotRequired[str]
    reference_for_beneficiary: NotRequired[str]
    review: NotRequired[TransferRequestReview2 | TransferRequestReview2Dict]
    type_: NotRequired[Type113OrStr]
    ultimate_party: NotRequired[UltimatePartyIdentification1 | UltimatePartyIdentification1Dict]
