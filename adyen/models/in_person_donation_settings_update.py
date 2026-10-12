from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .donation_amount_update import DonationAmountUpdate, DonationAmountUpdateDict
from .enums.display_text_field2 import DisplayTextField2OrStr
from .enums.donation_flow1 import DonationFlow1OrStr
from .enums.donation_type import DonationTypeOrStr


class InPersonDonationSettingsUpdate(SdkBaseModel):
    default_amount: OptionalNullable[DonationAmountUpdate] = Field(default=UNSET, alias="defaultAmount")
    """The default amount for donations."""

    display_text_field: Optional[DisplayTextField2OrStr] = Field(default=UNSET, alias="displayTextField")
    """The text shown on the payment terminal, either the name or the cause of the nonprofit organization."""

    donation_flow: Optional[DonationFlow1OrStr] = Field(default=UNSET, alias="donationFlow")
    """The interaction flow for in-person donations. Possible values:

    - **oneStep**: The shopper presents their payment method for the payment and the donation in one go, after the
        donation.

    - **twoStep**: The shopper presents their payment method twice: after the payment and after the donation."""

    donation_type: OptionalNullable[DonationTypeOrStr] = Field(default=UNSET, alias="donationType")
    """The type of donation to collect from the shopper. Possible values:

    - **roundup**: Round up the transaction amount.

    - **fixedAmounts**: Choose a fixed amount.

    - **fixedAmountsRoundup**: Round up, or choose a fixed amount."""

    merchant_accounts: OptionalNullable[list[str]] = Field(default=UNSET, alias="merchantAccounts")
    """The merchant accounts for this sales channel that are associated with the donation campaign."""

    present_card_timeout_ms: OptionalNullable[int] = Field(default=UNSET, alias="presentCardTimeoutMs")
    """Required if ``donationFlow`` is set to **twoStep**. The time, in milliseconds, that the terminal waits for the
    shopper to present their card. Defaults to **10000** (10 seconds). Range: 5000 to 15000."""

    prompt_timeout_ms: OptionalNullable[int] = Field(default=UNSET, alias="promptTimeoutMs")
    """The time, in milliseconds, that the terminal waits for the shopper to make a selection on the donation screen.
    Defaults to **10000** (10 seconds). Range: 5000 to 15000."""

    store_ids: OptionalNullable[list[str]] = Field(default=UNSET, alias="storeIds")
    """The Adyen-generated unique identifiers of stores for this sales channel that are associated with the donation
    campaign."""


class InPersonDonationSettingsUpdateDict(TypedDict):
    default_amount: NotRequired[DonationAmountUpdateDict | None]
    display_text_field: NotRequired[DisplayTextField2OrStr]
    donation_flow: NotRequired[DonationFlow1OrStr]
    donation_type: NotRequired[DonationTypeOrStr | None]
    merchant_accounts: NotRequired[list[str] | None]
    present_card_timeout_ms: NotRequired[int | None]
    prompt_timeout_ms: NotRequired[int | None]
    store_ids: NotRequired[list[str] | None]
