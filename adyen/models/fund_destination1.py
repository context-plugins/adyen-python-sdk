from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address import Address, AddressDict
from .card1 import Card1, Card1Dict
from .name import Name, NameDict
from .sub_merchant import SubMerchant, SubMerchantDict


class FundDestination1(SdkBaseModel):
    """the person or entity receiving the money"""

    iban: Optional[str] = Field(default=UNSET, alias="IBAN")
    """Bank Account Number of the recipient"""

    additional_data: Optional[dict[str, str]] = Field(default=UNSET, alias="additionalData")
    """a map of name/value pairs for passing in additional/industry-specific data"""

    billing_address: Optional[Address] = Field(default=UNSET, alias="billingAddress")
    """The address where to send the invoice."""

    card: Optional[Card1] = UNSET
    """Credit card data.

    Optional if ``shopperReference`` and ``selectedRecurringDetailReference`` are provided."""

    selected_recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="selectedRecurringDetailReference")
    """The ``recurringDetailReference`` you want to use for this payment. The value ``LATEST`` can be used to select the
    most recently stored recurring detail."""

    shopper_email: Optional[str] = Field(default=UNSET, alias="shopperEmail")
    """the email address of the person"""

    shopper_name: Optional[Name] = Field(default=UNSET, alias="shopperName")
    """the name of the person"""

    shopper_reference: Optional[str] = Field(default=UNSET, alias="shopperReference")
    """Required for recurring payments. Your reference to uniquely identify this shopper, for example user ID or account
    ID. The value is case-sensitive and must be at least three characters.
    > Your reference must not include personally identifiable information (PII) such as name or email address."""

    sub_merchant: Optional[SubMerchant] = Field(default=UNSET, alias="subMerchant")
    """Required for Back-to-Back/ purchase driven load in Wallet transactions. Contains the final merchant who will be
    receiving the money, also known as subMerchant, information."""

    telephone_number: Optional[str] = Field(default=UNSET, alias="telephoneNumber")
    """the telephone number of the person"""

    wallet_purpose: Optional[str] = Field(default=UNSET, alias="walletPurpose")
    """The purpose of a digital wallet transaction."""


class FundDestination1Dict(TypedDict):
    iban: NotRequired[str]
    additional_data: NotRequired[dict[str, str]]
    billing_address: NotRequired[AddressDict]
    card: NotRequired[Card1Dict]
    selected_recurring_detail_reference: NotRequired[str]
    shopper_email: NotRequired[str]
    shopper_name: NotRequired[NameDict]
    shopper_reference: NotRequired[str]
    sub_merchant: NotRequired[SubMerchantDict]
    telephone_number: NotRequired[str]
    wallet_purpose: NotRequired[str]
