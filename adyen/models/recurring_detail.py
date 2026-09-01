from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .address import Address, AddressDict
from .bank_account import BankAccount, BankAccountDict
from .card import Card, CardDict
from .name import Name, NameDict
from .token_details import TokenDetails, TokenDetailsDict


class RecurringDetail(SdkBaseModel):
    additional_data: Optional[dict[str, str]] = Field(default=UNSET, alias="additionalData")
    """This field contains additional data, which may be returned in a particular response.

    The additionalData object consists of entries, each of which includes the key and value."""

    alias: Optional[str] = UNSET
    """The alias of the credit card number.

    Applies only to recurring contracts storing credit card details"""

    alias_type: Optional[str] = Field(default=UNSET, alias="aliasType")
    """The alias type of the credit card number.

    Applies only to recurring contracts storing credit card details."""

    bank: Optional[BankAccount] = UNSET
    """A container for bank account data."""

    billing_address: Optional[Address] = Field(default=UNSET, alias="billingAddress")
    """The billing address."""

    card: Optional[Card] = UNSET
    """A container for card data."""

    contract_types: Optional[list[str]] = Field(default=UNSET, alias="contractTypes")
    """Types of recurring contracts."""

    creation_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="creationDate")
    """The date when the recurring details were created."""

    first_psp_reference: Optional[str] = Field(default=UNSET, alias="firstPspReference")
    """The ``pspReference`` of the first recurring payment that created the recurring detail."""

    name: Optional[str] = UNSET
    """An optional descriptive name for this recurring detail."""

    network_tx_reference: Optional[str] = Field(default=UNSET, alias="networkTxReference")
    """Returned in the response if you are not tokenizing with Adyen and are using the Merchant-initiated transactions
    (MIT) framework from Mastercard or Visa.

    This contains either the Mastercard Trace ID or the Visa Transaction ID."""

    payment_method_variant: Optional[str] = Field(default=UNSET, alias="paymentMethodVariant")
    """The type or sub-brand of a payment method used, e.g. Visa Debit, Visa Corporate, etc. For more information, refer
    to `PaymentMethodVariant <https://docs.adyen.com/development-resources/paymentmethodvariant>`__."""

    recurring_detail_reference: str = Field(alias="recurringDetailReference")
    """The reference that uniquely identifies the recurring detail."""

    shopper_name: Optional[Name] = Field(default=UNSET, alias="shopperName")
    """The name of the shopper."""

    social_security_number: Optional[str] = Field(default=UNSET, alias="socialSecurityNumber")
    """A shopper's social security number (only in countries where it is legal to collect)."""

    token_details: Optional[TokenDetails] = Field(default=UNSET, alias="tokenDetails")
    transaction_link_id: Optional[str] = Field(default=UNSET, alias="transactionLinkId")
    """The unique identifier for the transaction link, used for Mastercard recurring transactions."""

    variant: str
    """The payment method, such as “mc", "visa", "ideal", "paypal"."""


class RecurringDetailDict(TypedDict):
    additional_data: NotRequired[dict[str, str]]
    alias: NotRequired[str]
    alias_type: NotRequired[str]
    bank: NotRequired[BankAccount | BankAccountDict]
    billing_address: NotRequired[Address | AddressDict]
    card: NotRequired[Card | CardDict]
    contract_types: NotRequired[list[str]]
    creation_date: NotRequired[RFC3339DateTime]
    first_psp_reference: NotRequired[str]
    name: NotRequired[str]
    network_tx_reference: NotRequired[str]
    payment_method_variant: NotRequired[str]
    recurring_detail_reference: str
    shopper_name: NotRequired[Name | NameDict]
    social_security_number: NotRequired[str]
    token_details: NotRequired[TokenDetails | TokenDetailsDict]
    transaction_link_id: NotRequired[str]
    variant: str
