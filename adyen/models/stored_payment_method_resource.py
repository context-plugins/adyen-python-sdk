from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .address5 import Address5, Address5Dict
from .token_mandate2 import TokenMandate2, TokenMandate2Dict


class StoredPaymentMethodResource(SdkBaseModel):
    alias: Optional[str] = UNSET
    """The alias of the credit card number.

    Applies only to recurring contracts storing credit card details"""

    alias_type: Optional[str] = Field(default=UNSET, alias="aliasType")
    """The alias type of the credit card number.

    Applies only to recurring contracts storing credit card details."""

    billing_address: Optional[Address5] = Field(default=UNSET, alias="billingAddress")
    """The billing address associated with the stored payment method."""

    brand: Optional[str] = UNSET
    """The brand of the card."""

    card_bin: Optional[str] = Field(default=UNSET, alias="cardBin")
    """The bank identification number (BIN) of the card."""

    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    """The date when the recurring details were created."""

    expiry_month: Optional[str] = Field(default=UNSET, alias="expiryMonth")
    """The month the card expires."""

    expiry_year: Optional[str] = Field(default=UNSET, alias="expiryYear")
    """The last two digits of the year the card expires. For example, **22** for the year 2022."""

    external_response_code: Optional[str] = Field(default=UNSET, alias="externalResponseCode")
    """The response code returned by an external system (for example after a provisioning operation)."""

    external_token_reference: Optional[str] = Field(default=UNSET, alias="externalTokenReference")
    """The token reference of a linked token in an external system (for example a network token reference)."""

    first_psp_reference: Optional[str] = Field(default=UNSET, alias="firstPspReference")
    """The PSP reference of the first payment that created this recurring detail."""

    holder_name: Optional[str] = Field(default=UNSET, alias="holderName")
    """The unique payment method code."""

    iban: Optional[str] = UNSET
    """The IBAN of the bank account."""

    id: Optional[str] = UNSET
    """A unique identifier of this stored payment method."""

    issuer_name: Optional[str] = Field(default=UNSET, alias="issuerName")
    """The name of the issuer of token or card."""

    last_four: Optional[str] = Field(default=UNSET, alias="lastFour")
    """The last four digits of the PAN."""

    mandate: Optional[TokenMandate2] = UNSET
    """Mandate details for the stored payment method."""

    name: Optional[str] = UNSET
    """The display name of the stored payment method."""

    network_tx_reference: Optional[str] = Field(default=UNSET, alias="networkTxReference")
    """Returned in the response if you are not tokenizing with Adyen and are using the Merchant-initiated transactions
    (MIT) framework from Mastercard or Visa.

    This contains either the Mastercard Trace ID or the Visa Transaction ID."""

    owner_name: Optional[str] = Field(default=UNSET, alias="ownerName")
    """The name of the bank account holder."""

    shopper_email: Optional[str] = Field(default=UNSET, alias="shopperEmail")
    """The shopper’s email address."""

    shopper_reference: Optional[str] = Field(default=UNSET, alias="shopperReference")
    """Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive
    and must be at least three characters.
    > Your reference must not include personally identifiable information (PII) such as name or email address."""

    supported_recurring_processing_models: Optional[list[str]] = Field(
        default=UNSET, alias="supportedRecurringProcessingModels"
    )
    """Defines a recurring payment type. Allowed values:
    * ``Subscription`` – A transaction for a fixed or variable amount, which follows a fixed schedule.
    * ``CardOnFile`` – With a card-on-file (CoF) transaction, card details are stored to enable one-click or omnichannel
        journeys, or simply to streamline the checkout process. Any subscription not following a fixed schedule is also
        considered a card-on-file transaction.
    * ``UnscheduledCardOnFile`` – An unscheduled card-on-file (UCoF) transaction is a transaction that occurs on a
        non-fixed schedule and/or have variable amounts. For example, automatic top-ups when a cardholder's balance
        drops below a certain amount."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The type of payment method."""


class StoredPaymentMethodResourceDict(TypedDict):
    alias: NotRequired[str]
    alias_type: NotRequired[str]
    billing_address: NotRequired[Address5 | Address5Dict]
    brand: NotRequired[str]
    card_bin: NotRequired[str]
    created_at: NotRequired[RFC3339DateTime]
    expiry_month: NotRequired[str]
    expiry_year: NotRequired[str]
    external_response_code: NotRequired[str]
    external_token_reference: NotRequired[str]
    first_psp_reference: NotRequired[str]
    holder_name: NotRequired[str]
    iban: NotRequired[str]
    id: NotRequired[str]
    issuer_name: NotRequired[str]
    last_four: NotRequired[str]
    mandate: NotRequired[TokenMandate2 | TokenMandate2Dict]
    name: NotRequired[str]
    network_tx_reference: NotRequired[str]
    owner_name: NotRequired[str]
    shopper_email: NotRequired[str]
    shopper_reference: NotRequired[str]
    supported_recurring_processing_models: NotRequired[list[str]]
    type_: NotRequired[str]
