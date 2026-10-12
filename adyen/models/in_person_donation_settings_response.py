from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .donation_amount import DonationAmount, DonationAmountDict
from .enums.display_text_field1 import DisplayTextField1OrStr
from .enums.donation_flow4 import DonationFlow4OrStr
from .enums.donation_type1 import DonationType1OrStr


class InPersonDonationSettingsResponse(SdkBaseModel):
    amounts: Optional[list[DonationAmount]] = UNSET
    """The currency and fixed amounts for donations. We automatically add calculated amounts in other currencies for
    participating stores that use a different currency than the default."""

    default_currency: Optional[str] = Field(default=UNSET, alias="defaultCurrency")
    """The currency that was used in the request to set fixed donation amounts. Format: three-character `ISO currency
    code <https://docs.adyen.com/development-resources/currency-codes#currency-codes>`__."""

    display_text_field: Optional[DisplayTextField1OrStr] = Field(default=UNSET, alias="displayTextField")
    """The text shown on the payment terminal, asking the shopper for a donation."""

    donation_flow: Optional[DonationFlow4OrStr] = Field(default=UNSET, alias="donationFlow")
    """The interaction flow for in-person donations: complete payment for the purchase and the donation in one go, or
    separately."""

    donation_type: Optional[DonationType1OrStr] = Field(default=UNSET, alias="donationType")
    """The type of donation to collect from the shopper. Possible values:

    - **roundup**: Round up the transaction amount.

    - **fixedAmounts**: Choose a fixed amount.

    - **fixedAmountsRoundup**: Round up, or choose a fixed amount."""

    merchant_accounts: Optional[list[str]] = Field(default=UNSET, alias="merchantAccounts")
    """The merchant accounts for this sales channel that are associated with the donation campaign."""

    present_card_timeout_ms: Optional[int] = Field(default=UNSET, alias="presentCardTimeoutMs")
    """The time, in milliseconds, that the terminal waits for the shopper to present their card."""

    prompt_timeout_ms: Optional[int] = Field(default=UNSET, alias="promptTimeoutMs")
    """The time, in milliseconds, that the terminal waits for the shopper to respond to the text asking for a
    donation."""

    store_ids: Optional[list[str]] = Field(default=UNSET, alias="storeIds")
    """The Adyen-generated unique identifiers of stores for this sales channel that are associated with the donation
    campaign."""


class InPersonDonationSettingsResponseDict(TypedDict):
    amounts: NotRequired[list[DonationAmountDict]]
    default_currency: NotRequired[str]
    display_text_field: NotRequired[DisplayTextField1OrStr]
    donation_flow: NotRequired[DonationFlow4OrStr]
    donation_type: NotRequired[DonationType1OrStr]
    merchant_accounts: NotRequired[list[str]]
    present_card_timeout_ms: NotRequired[int]
    prompt_timeout_ms: NotRequired[int]
    store_ids: NotRequired[list[str]]
