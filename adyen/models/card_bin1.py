from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CardBin1(SdkBaseModel):
    """Card BIN details."""

    bin: Optional[str] = UNSET
    """The first 6 digit of the card number. Enable this field via merchant account settings."""

    commercial: Optional[bool] = UNSET
    """If true, it indicates a commercial card. Enable this field via merchant account settings."""

    funding_source: Optional[str] = Field(default=UNSET, alias="fundingSource")
    """The card funding source. Valid values are:
    * CHARGE
    * CREDIT
    * DEBIT
    * DEFERRED_DEBIT
    * PREPAID
    * PREPAID_RELOADABLE
    * PREPAID_NONRELOADABLE
    > Enable this field via merchant account settings."""

    funds_availability: Optional[str] = Field(default=UNSET, alias="fundsAvailability")
    """Indicates availability of funds.

    Visa:
    * "I" (fast funds are supported)
    * "N" (otherwise)

    Mastercard:
    * "I" (product type is Prepaid or Debit, or issuing country is in CEE/HGEM list)
    * "N" (otherwise)
    > Returned when you verify a card BIN or estimate costs, and only if ``payoutEligible`` is different from "N" or
        "U"."""

    issuer_bin: Optional[str] = Field(default=UNSET, alias="issuerBin")
    """The first 8 digit of the card number. Enable this field via merchant account settings."""

    issuing_bank: Optional[str] = Field(default=UNSET, alias="issuingBank")
    """The issuing bank of the card."""

    issuing_country: Optional[str] = Field(default=UNSET, alias="issuingCountry")
    """The country where the card was issued from."""

    issuing_currency: Optional[str] = Field(default=UNSET, alias="issuingCurrency")
    """The currency of the card."""

    payment_method: Optional[str] = Field(default=UNSET, alias="paymentMethod")
    """The payment method associated with the card (e.g. visa, mc, or amex)."""

    payout_eligible: Optional[str] = Field(default=UNSET, alias="payoutEligible")
    """Indicates whether a payout is eligible or not for this card.

    Visa:
    * "Y"
    * "N"

    Mastercard:
    * "Y" (domestic and cross-border)
    * "D" (only domestic)
    * "N" (no MoneySend)
    * "U" (unknown)
    > Returned when you verify a card BIN or estimate costs, and only if ``payoutEligible`` is different from "N" or
        "U"."""

    summary: Optional[str] = UNSET
    """The last four digits of the card number."""


class CardBin1Dict(TypedDict):
    bin: NotRequired[str]
    commercial: NotRequired[bool]
    funding_source: NotRequired[str]
    funds_availability: NotRequired[str]
    issuer_bin: NotRequired[str]
    issuing_bank: NotRequired[str]
    issuing_country: NotRequired[str]
    issuing_currency: NotRequired[str]
    payment_method: NotRequired[str]
    payout_eligible: NotRequired[str]
    summary: NotRequired[str]
