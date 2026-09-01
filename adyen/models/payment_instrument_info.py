from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bank_account_model1 import BankAccountModel1, BankAccountModel1Dict
from .card_info1 import CardInfo1, CardInfo1Dict
from .enums.status10 import Status10OrStr
from .enums.status_reason import StatusReasonOrStr
from .enums.type111 import Type111OrStr


class PaymentInstrumentInfo(SdkBaseModel):
    balance_account_id: str = Field(alias="balanceAccountId")
    """The unique identifier of the `balance account
    <https://docs.adyen.com/api-explorer/#/balanceplatform/v1/post/balanceAccounts__resParam_id>`__ associated with the
    payment instrument."""

    bank_account: Optional[BankAccountModel1] = Field(default=UNSET, alias="bankAccount")
    """Contains the business account details."""

    card: Optional[CardInfo1] = UNSET
    """Contains information about the card. Required when you create a payment instrument of ``type`` **card**."""

    description: Optional[str] = UNSET
    """Your description for the payment instrument, maximum 300 characters."""

    issuing_country_code: str = Field(alias="issuingCountryCode")
    """The two-character `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code where
    the payment instrument is issued. For example, **NL** or **US**."""

    payment_instrument_group_id: Optional[str] = Field(default=UNSET, alias="paymentInstrumentGroupId")
    """The unique identifier of the `payment instrument group
    <https://docs.adyen.com/api-explorer/#/balanceplatform/v1/post/paymentInstrumentGroups__resParam_id>`__ to which the
    payment instrument belongs."""

    reference: Optional[str] = UNSET
    """Your reference for the payment instrument, maximum 150 characters."""

    status: Optional[Status10OrStr] = UNSET
    """The status of the payment instrument. If a status is not specified when creating a payment instrument, it is set
    to **active** by default. However, there can be exceptions for cards based on the ``card.formFactor`` and the
    ``issuingCountryCode``. For example, when issuing physical cards in the US, the default status is **inactive**.

    Possible values:

     * **active**: The payment instrument is active and can be used to make payments.

     * **inactive**: The payment instrument is inactive and cannot be used to make payments.

     * **suspended**: The payment instrument is suspended, either because it was stolen or lost.

     * **closed**: The payment instrument is permanently closed. This action cannot be undone."""

    status_comment: Optional[str] = Field(default=UNSET, alias="statusComment")
    """The status comment provides additional information for the statusReason of the payment instrument."""

    status_reason: Optional[StatusReasonOrStr] = Field(default=UNSET, alias="statusReason")
    """The reason for the status of the payment instrument.

    Possible values: **accountClosure**, **damaged**, **endOfLife**, **expired**, **lost**, **stolen**,
    **suspectedFraud**, **transactionRule**, **other**. If the reason is **other**, you must also send the
    ``statusComment`` parameter describing the status change."""

    type_: Type111OrStr = Field(alias="type")
    """The type of payment instrument.

    Possible values: **card**, **bankAccount**."""


class PaymentInstrumentInfoDict(TypedDict):
    balance_account_id: str
    bank_account: NotRequired[BankAccountModel1 | BankAccountModel1Dict]
    card: NotRequired[CardInfo1 | CardInfo1Dict]
    description: NotRequired[str]
    issuing_country_code: str
    payment_instrument_group_id: NotRequired[str]
    reference: NotRequired[str]
    status: NotRequired[Status10OrStr]
    status_comment: NotRequired[str]
    status_reason: NotRequired[StatusReasonOrStr]
    type_: Type111OrStr
