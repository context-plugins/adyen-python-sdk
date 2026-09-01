from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Card(SdkBaseModel):
    """A container for card data., Credit card data.

    Optional if ``shopperReference`` and ``selectedRecurringDetailReference`` are provided., Credit card data.

    Optional if ``shopperReference`` and ``selectedRecurringDetailReference`` are provided., A container for card data.
    > Either ``bankAccount`` or ``card`` field must be provided in a payment request., A container for card data.
    > This field is mandatory if ``bank`` is not provided."""

    cvc: Optional[str] = UNSET
    """The `card verification code
    <https://docs.adyen.com/payments-fundamentals/payment-glossary#card-security-code-cvc-cvv-cid>`__ (1-20 characters).
    Depending on the card brand, it is known also as:
    * CVV2/CVC2 – length: 3 digits
    * CID – length: 4 digits
    > If you are using `Client-Side Encryption
        <https://docs.adyen.com/classic-integration/cse-integration-ecommerce>`__, the CVC code is present in the
        encrypted data. You must never post the card details to the server.
    > This field must be always present in a `one-click payment request
        <https://docs.adyen.com/classic-integration/recurring-payments>`__.
    > When this value is returned in a response, it is always empty because it is not stored."""

    expiry_month: Optional[str] = Field(default=UNSET, alias="expiryMonth")
    """The card expiry month. Format: 2 digits, zero-padded for single digits. For example:
    * 03 = March
    * 11 = November"""

    expiry_year: Optional[str] = Field(default=UNSET, alias="expiryYear")
    """The card expiry year. Format: 4 digits. For example: 2020"""

    holder_name: Optional[str] = Field(default=UNSET, alias="holderName")
    """The name of the cardholder, as printed on the card."""

    issue_number: Optional[str] = Field(default=UNSET, alias="issueNumber")
    """The issue number of the card (for some UK debit cards only)."""

    number: Optional[str] = UNSET
    """The card number (4-19 characters). Do not use any separators. When this value is returned in a response, only the
    last 4 digits of the card number are returned."""

    start_month: Optional[str] = Field(default=UNSET, alias="startMonth")
    """The month component of the start date (for some UK debit cards only)."""

    start_year: Optional[str] = Field(default=UNSET, alias="startYear")
    """The year component of the start date (for some UK debit cards only)."""


class CardDict(TypedDict):
    cvc: NotRequired[str]
    expiry_month: NotRequired[str]
    expiry_year: NotRequired[str]
    holder_name: NotRequired[str]
    issue_number: NotRequired[str]
    number: NotRequired[str]
    start_month: NotRequired[str]
    start_year: NotRequired[str]
