from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .donation_amount_update import DonationAmountUpdate, DonationAmountUpdateDict
from .enums.donation_type import DonationTypeOrStr


class OnlineDonationSettingsUpdate(SdkBaseModel):
    default_amount: OptionalNullable[DonationAmountUpdate] = Field(default=UNSET, alias="defaultAmount")
    """The default amount for donations."""

    donation_type: OptionalNullable[DonationTypeOrStr] = Field(default=UNSET, alias="donationType")
    """The type of donation to collect from the shopper. Possible values:

    - **roundup**: Round up the transaction amount.

    - **fixedAmounts**: Choose a fixed amount.

    - **fixedAmountsRoundup**: Round up, or choose a fixed amount."""

    merchant_accounts: Optional[list[str | None]] = Field(default=UNSET, alias="merchantAccounts")
    """The merchant accounts for this sales channel that are associated with the donation campaign."""

    store_ids: Optional[list[str | None]] = Field(default=UNSET, alias="storeIds")
    """The Adyen-generated unique identifiers of stores for this sales channel that are associated with the donation
    campaign."""


class OnlineDonationSettingsUpdateDict(TypedDict):
    default_amount: NotRequired[DonationAmountUpdate | DonationAmountUpdateDict | None]
    donation_type: NotRequired[DonationTypeOrStr | None]
    merchant_accounts: NotRequired[list[str | None]]
    store_ids: NotRequired[list[str | None]]
