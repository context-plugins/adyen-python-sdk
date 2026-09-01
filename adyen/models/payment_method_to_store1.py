from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PaymentMethodToStore1(SdkBaseModel):
    """Contains the information required to store a payment method."""

    brand: Optional[str] = UNSET
    """Secondary brand of the card. For example: **plastix**, **hmclub**."""

    cvc: Optional[str] = UNSET
    """The card verification code. Only collect raw card data if you are `fully PCI compliant
    <https://docs.adyen.com/development-resources/pci-dss-compliance-guide>`__."""

    encrypted_card: Optional[str] = Field(default=UNSET, alias="encryptedCard")
    """The encrypted card."""

    encrypted_card_number: Optional[str] = Field(default=UNSET, alias="encryptedCardNumber")
    """The encrypted card number."""

    encrypted_expiry_month: Optional[str] = Field(default=UNSET, alias="encryptedExpiryMonth")
    """The encrypted card expiry month."""

    encrypted_expiry_year: Optional[str] = Field(default=UNSET, alias="encryptedExpiryYear")
    """The encrypted card expiry year."""

    encrypted_security_code: Optional[str] = Field(default=UNSET, alias="encryptedSecurityCode")
    """The encrypted card verification code."""

    expiry_month: Optional[str] = Field(default=UNSET, alias="expiryMonth")
    """The card expiry month. Only collect raw card data if you are `fully PCI compliant
    <https://docs.adyen.com/development-resources/pci-dss-compliance-guide>`__."""

    expiry_year: Optional[str] = Field(default=UNSET, alias="expiryYear")
    """The card expiry year. Only collect raw card data if you are `fully PCI compliant
    <https://docs.adyen.com/development-resources/pci-dss-compliance-guide>`__."""

    holder_name: Optional[str] = Field(default=UNSET, alias="holderName")
    """The name of the card holder."""

    number: Optional[str] = UNSET
    """The card number. Only collect raw card data if you are `fully PCI compliant
    <https://docs.adyen.com/development-resources/pci-dss-compliance-guide>`__."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Set to **scheme**."""


class PaymentMethodToStore1Dict(TypedDict):
    brand: NotRequired[str]
    cvc: NotRequired[str]
    encrypted_card: NotRequired[str]
    encrypted_card_number: NotRequired[str]
    encrypted_expiry_month: NotRequired[str]
    encrypted_expiry_year: NotRequired[str]
    encrypted_security_code: NotRequired[str]
    expiry_month: NotRequired[str]
    expiry_year: NotRequired[str]
    holder_name: NotRequired[str]
    number: NotRequired[str]
    type_: NotRequired[str]
