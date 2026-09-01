from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CardDetailsRequest(SdkBaseModel):
    card_number: Optional[str] = Field(default=UNSET, alias="cardNumber")
    """A minimum of the first six digits of the card number. The full card number gives the best result.

    You must be `fully PCI compliant <https://docs.adyen.com/development-resources/pci-dss-compliance-guide>`__ to
    collect raw card data. Alternatively, you can use the ``encryptedCardNumber`` field."""

    country_code: Optional[str] = Field(default=UNSET, alias="countryCode")
    """The shopper country code.

    Format: `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ Example: NL or DE"""

    encrypted_card_number: Optional[str] = Field(default=UNSET, alias="encryptedCardNumber")
    """The encrypted card number."""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier, with which you want to process the transaction."""

    supported_brands: Optional[list[str]] = Field(default=UNSET, alias="supportedBrands")
    """The card brands you support. This is the
    https://docs.adyen.com/api-explorer/Checkout/latest/post/paymentMethods#responses-200-paymentMethods-brands array
    from your https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/paymentMethods response.

    If not included, our API uses the ones configured for your merchant account and, if provided, the country code."""


class CardDetailsRequestDict(TypedDict):
    card_number: NotRequired[str]
    country_code: NotRequired[str]
    encrypted_card_number: NotRequired[str]
    merchant_account: str
    supported_brands: NotRequired[list[str]]
