from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bank_account_details1 import BankAccountDetails1, BankAccountDetails1Dict
from .card11 import Card11, Card11Dict
from .enums.status10 import Status10OrStr
from .enums.status_reason import StatusReasonOrStr
from .enums.type111 import Type111OrStr
from .iban_account_identification import IbanAccountIdentification, IbanAccountIdentificationDict


class UpdatePaymentInstrument(SdkBaseModel):
    additional_bank_account_identifications: Optional[list[IbanAccountIdentification]] = Field(
        default=UNSET, alias="additionalBankAccountIdentifications"
    )
    """Contains optional, additional business account details. Returned when you create a payment instrument with
    ``type`` **bankAccount**."""

    balance_account_id: str = Field(alias="balanceAccountId")
    """The unique identifier of the `balance account
    <https://docs.adyen.com/api-explorer/#/balanceplatform/v1/post/balanceAccounts__resParam_id>`__ associated with the
    payment instrument."""

    bank_account: Optional[BankAccountDetails1] = Field(default=UNSET, alias="bankAccount")
    """Contains the business account details. Returned when you create a payment instrument with ``type``
    **bankAccount**."""

    card: Optional[Card11] = UNSET
    """Contains information about the card payment instrument. Returned when you create a payment instrument with
    ``type`` **card**."""

    description: Optional[str] = UNSET
    """Your description for the payment instrument, maximum 300 characters."""

    id: str
    """The unique identifier of the payment instrument."""

    issuing_country_code: str = Field(alias="issuingCountryCode")
    """The two-character `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code where
    the payment instrument is issued. For example, **NL** or **US**."""

    payment_instrument_group_id: Optional[str] = Field(default=UNSET, alias="paymentInstrumentGroupId")
    """The unique identifier of the `payment instrument group
    <https://docs.adyen.com/api-explorer/#/balanceplatform/v1/post/paymentInstrumentGroups__resParam_id>`__ to which the
    payment instrument belongs."""

    reference: Optional[str] = UNSET
    """Your reference for the payment instrument, maximum 150 characters."""

    replaced_by_id: Optional[str] = Field(default=UNSET, alias="replacedById")
    """The unique identifier of the payment instrument that replaced this payment instrument."""

    replacement_of_id: Optional[str] = Field(default=UNSET, alias="replacementOfId")
    """The unique identifier of the payment instrument that is replaced by this payment instrument."""

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
    """Comment for the status of the payment instrument.

    Required if ``statusReason`` is **other**."""

    status_reason: Optional[StatusReasonOrStr] = Field(default=UNSET, alias="statusReason")
    """The reason for the status of the payment instrument.

    Possible values: **accountClosure**, **damaged**, **endOfLife**, **expired**, **lost**, **stolen**,
    **suspectedFraud**, **transactionRule**, **other**. If the reason is **other**, you must also send the
    ``statusComment`` parameter describing the status change."""

    type_: Type111OrStr = Field(alias="type")
    """The type of payment instrument.

    Possible values: **card**, **bankAccount**."""


class UpdatePaymentInstrumentDict(TypedDict):
    additional_bank_account_identifications: NotRequired[
        list[IbanAccountIdentification | IbanAccountIdentificationDict]
    ]
    balance_account_id: str
    bank_account: NotRequired[BankAccountDetails1 | BankAccountDetails1Dict]
    card: NotRequired[Card11 | Card11Dict]
    description: NotRequired[str]
    id: str
    issuing_country_code: str
    payment_instrument_group_id: NotRequired[str]
    reference: NotRequired[str]
    replaced_by_id: NotRequired[str]
    replacement_of_id: NotRequired[str]
    status: NotRequired[Status10OrStr]
    status_comment: NotRequired[str]
    status_reason: NotRequired[StatusReasonOrStr]
    type_: Type111OrStr
