from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .donation_amount1 import DonationAmount1, DonationAmount1Dict
from .enums.donation_type1 import DonationType1OrStr


class OnlineDonationSettings2(SdkBaseModel):
    """The settings for online donations collected as part of the campaign."""

    default_amount: Optional[DonationAmount1] = Field(default=UNSET, alias="defaultAmount")
    """The default amount for donations."""

    donation_type: Optional[DonationType1OrStr] = Field(default=UNSET, alias="donationType")
    """The type of donation to collect from the shopper. Possible values:

    - **roundup**: Round up the transaction amount.

    - **fixedAmounts**: Choose a fixed amount.

    - **fixedAmountsRoundup**: Round up, or choose a fixed amount."""

    merchant_accounts: Optional[list[str]] = Field(default=UNSET, alias="merchantAccounts")
    """The merchant accounts for this sales channel that are associated with the donation campaign."""

    store_ids: Optional[list[str]] = Field(default=UNSET, alias="storeIds")
    """The Adyen-generated unique identifiers of stores for this sales channel that are associated with the donation
    campaign."""


class OnlineDonationSettings2Dict(TypedDict):
    default_amount: NotRequired[DonationAmount1 | DonationAmount1Dict]
    donation_type: NotRequired[DonationType1OrStr]
    merchant_accounts: NotRequired[list[str]]
    store_ids: NotRequired[list[str]]
