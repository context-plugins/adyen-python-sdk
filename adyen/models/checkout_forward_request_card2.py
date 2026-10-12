from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type18 import Type18, Type18OrStr


class CheckoutForwardRequestCard2(SdkBaseModel):
    """The card details."""

    cvc: Optional[str] = UNSET
    """The `card verification code
    <https://docs.adyen.com/payments-fundamentals/payment-glossary#card-security-code-cvc-cvv-cid>`__ (1-20 characters).
    Depending on the card brand, it is also known as:
    * CVV2/CVC2 – length: 3 digits
    * CID – length: 4 digits"""

    encrypted_card_number: Optional[str] = Field(default=UNSET, alias="encryptedCardNumber")
    """The encrypted card number."""

    encrypted_expiry_month: Optional[str] = Field(default=UNSET, alias="encryptedExpiryMonth")
    """The encrypted expiryMonth"""

    encrypted_expiry_year: Optional[str] = Field(default=UNSET, alias="encryptedExpiryYear")
    """The encrypted card expiry year."""

    encrypted_security_code: Optional[str] = Field(default=UNSET, alias="encryptedSecurityCode")
    """The encrypted security code."""

    expiry_month: Optional[str] = Field(default=UNSET, alias="expiryMonth")
    """The card expiry month. Format: 2 digits, zero-padded for single digits. For example:
    * 03 = March
    * 11 = November"""

    expiry_year: Optional[str] = Field(default=UNSET, alias="expiryYear")
    """The card expiry year."""

    holder_name: Optional[str] = Field(default=UNSET, alias="holderName")
    """The name of the cardholder."""

    number: Optional[str] = UNSET
    """The card number. Only collect raw card data if you are fully `PCI compliant
    <https://docs.adyen.com/development-resources/pci-dss-compliance-guide>`__. Format: Do not use separators."""

    type_: Type18OrStr = Field(default=Type18.SCHEME, alias="type")
    """Default payment method details. Common for scheme payment methods, and for simple payment method details."""


class CheckoutForwardRequestCard2Dict(TypedDict):
    cvc: NotRequired[str]
    encrypted_card_number: NotRequired[str]
    encrypted_expiry_month: NotRequired[str]
    encrypted_expiry_year: NotRequired[str]
    encrypted_security_code: NotRequired[str]
    expiry_month: NotRequired[str]
    expiry_year: NotRequired[str]
    holder_name: NotRequired[str]
    number: NotRequired[str]
    type_: NotRequired[Type18OrStr]
