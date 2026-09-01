from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .donation_amount1 import DonationAmount1, DonationAmount1Dict
from .enums.display_text_field2 import DisplayTextField2OrStr
from .enums.donation_flow1 import DonationFlow1OrStr
from .enums.donation_type1 import DonationType1OrStr


class InPersonDonationSettings2(SdkBaseModel):
    """The settings for in-person donations collected as part of the campaign."""

    default_amount: Optional[DonationAmount1] = Field(default=UNSET, alias="defaultAmount")
    """The default amount for donations."""

    display_text_field: DisplayTextField2OrStr = Field(alias="displayTextField")
    """The text shown on the payment terminal, either the name or the cause of the nonprofit organization."""

    donation_flow: DonationFlow1OrStr = Field(alias="donationFlow")
    """The interaction flow for in-person donations. Possible values:

    - **oneStep**: The shopper presents their payment method for the payment and the donation in one go, after the
        donation.

    - **twoStep**: The shopper presents their payment method twice: after the payment and after the donation."""

    donation_type: Optional[DonationType1OrStr] = Field(default=UNSET, alias="donationType")
    """The type of donation to collect from the shopper. Possible values:

    - **roundup**: Round up the transaction amount.

    - **fixedAmounts**: Choose a fixed amount.

    - **fixedAmountsRoundup**: Round up, or choose a fixed amount."""

    merchant_accounts: Optional[list[str]] = Field(default=UNSET, alias="merchantAccounts")
    """The merchant accounts for this sales channel that are associated with the donation campaign."""

    present_card_timeout_ms: Optional[int] = Field(default=UNSET, alias="presentCardTimeoutMs")
    """Required if ``donationFlow`` is set to **twoStep**. The time, in milliseconds, that the terminal waits for the
    shopper to present their card. Defaults to **10000** (10 seconds). Range: 5000 to 15000."""

    prompt_timeout_ms: Optional[int] = Field(default=UNSET, alias="promptTimeoutMs")
    """The time, in milliseconds, that the terminal waits for the shopper to make a selection on the donation screen.
    Defaults to **10000** (10 seconds). Range: 5000 to 15000."""

    store_ids: Optional[list[str]] = Field(default=UNSET, alias="storeIds")
    """The Adyen-generated unique identifiers of stores for this sales channel that are associated with the donation
    campaign."""


class InPersonDonationSettings2Dict(TypedDict):
    default_amount: NotRequired[DonationAmount1 | DonationAmount1Dict]
    display_text_field: DisplayTextField2OrStr
    donation_flow: DonationFlow1OrStr
    donation_type: NotRequired[DonationType1OrStr]
    merchant_accounts: NotRequired[list[str]]
    present_card_timeout_ms: NotRequired[int]
    prompt_timeout_ms: NotRequired[int]
    store_ids: NotRequired[list[str]]
