from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .address import Address, AddressDict
from .amount import Amount, AmountDict
from .bank_account import BankAccount, BankAccountDict
from .card import Card, CardDict
from .enums.entity_type1 import EntityType1OrStr
from .name import Name, NameDict
from .recurring import Recurring, RecurringDict


class StoreDetailAndSubmitRequest(SdkBaseModel):
    additional_data: Optional[dict[str, str]] = Field(default=UNSET, alias="additionalData")
    """This field contains additional data, which may be required for a particular request."""

    amount: Amount
    """A container object for the payable amount information of the transaction."""

    bank: Optional[BankAccount] = UNSET
    """A container for bank account data.
    > This field is mandatory if ``card`` is not provided."""

    billing_address: Optional[Address] = Field(default=UNSET, alias="billingAddress")
    """The billing address.

    > The ``billingAddress`` object is required for cross-border payouts to and from Canada. Include all of the fields
        within this object."""

    card: Optional[Card] = UNSET
    """A container for card data.
    > This field is mandatory if ``bank`` is not provided."""

    date_of_birth: Date = Field(alias="dateOfBirth")
    """The date of birth. Format: `ISO-8601 <https://www.w3.org/TR/NOTE-datetime>`__; example: YYYY-MM-DD For
    Paysafecard it must be the same as used when registering the Paysafecard account.
    > This field is mandatory for natural persons."""

    entity_type: EntityType1OrStr = Field(alias="entityType")
    """The type of the entity the payout is processed for."""

    fraud_offset: Optional[int] = Field(default=UNSET, alias="fraudOffset")
    """An integer value that is added to the normal fraud score. The value can be either positive or negative."""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier, with which you want to process the transaction."""

    nationality: str
    """The shopper's nationality.

    A valid value is an ISO 2-character country code (e.g. 'NL')."""

    recurring: Recurring
    """A container for the type of recurring contract to be retrieved.

    The recurring.contract must be set to ``PAYOUT``"""

    reference: str
    """The merchant reference for this payment. This reference will be used in all communication to the merchant about
    the status of the payout. Although it is a good idea to make sure it is unique, this is not a requirement."""

    selected_brand: Optional[str] = Field(default=UNSET, alias="selectedBrand")
    """The name of the brand to make a payout to.

    For Paysafecard it must be set to ``paysafecard``."""

    shopper_email: str = Field(alias="shopperEmail")
    """The shopper's email address."""

    shopper_name: Optional[Name] = Field(default=UNSET, alias="shopperName")
    """The shopper's name.

    When the ``entityType`` is ``Company``, the ``shopperName.lastName`` must contain the company name."""

    shopper_reference: str = Field(alias="shopperReference")
    """The shopper's reference for the payment transaction."""

    shopper_statement: Optional[str] = Field(default=UNSET, alias="shopperStatement")
    """The description of this payout. This description is shown on the bank statement of the shopper (if this is
    supported by the chosen payment method)."""

    social_security_number: Optional[str] = Field(default=UNSET, alias="socialSecurityNumber")
    """The shopper's social security number."""

    telephone_number: Optional[str] = Field(default=UNSET, alias="telephoneNumber")
    """The shopper's phone number."""


class StoreDetailAndSubmitRequestDict(TypedDict):
    additional_data: NotRequired[dict[str, str]]
    amount: AmountDict
    bank: NotRequired[BankAccountDict]
    billing_address: NotRequired[AddressDict]
    card: NotRequired[CardDict]
    date_of_birth: Date
    entity_type: EntityType1OrStr
    fraud_offset: NotRequired[int]
    merchant_account: str
    nationality: str
    recurring: RecurringDict
    reference: str
    selected_brand: NotRequired[str]
    shopper_email: str
    shopper_name: NotRequired[NameDict]
    shopper_reference: str
    shopper_statement: NotRequired[str]
    social_security_number: NotRequired[str]
    telephone_number: NotRequired[str]
