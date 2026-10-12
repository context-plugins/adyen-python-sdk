from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .donation_amount import DonationAmount, DonationAmountDict
from .enums.donation_type1 import DonationType1OrStr


class OnlineDonationSettingsResponse(SdkBaseModel):
    amounts: Optional[list[DonationAmount]] = UNSET
    """The currency and fixed amounts for donations. We automatically add calculated amounts in other currencies for
    participating stores that use a different currency than the default."""

    default_currency: Optional[str] = Field(default=UNSET, alias="defaultCurrency")
    """The currency that was used in the request to set fixed donation amounts. Format: three-character `ISO currency
    code <https://docs.adyen.com/development-resources/currency-codes#currency-codes>`__."""

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


class OnlineDonationSettingsResponseDict(TypedDict):
    amounts: NotRequired[list[DonationAmountDict]]
    default_currency: NotRequired[str]
    donation_type: NotRequired[DonationType1OrStr]
    merchant_accounts: NotRequired[list[str]]
    store_ids: NotRequired[list[str]]
