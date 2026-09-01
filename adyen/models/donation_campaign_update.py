from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .in_person_donation_settings_update import InPersonDonationSettingsUpdate, InPersonDonationSettingsUpdateDict
from .online_donation_settings_update import OnlineDonationSettingsUpdate, OnlineDonationSettingsUpdateDict


class DonationCampaignUpdate(SdkBaseModel):
    account_holder_ids: Optional[list[str | None]] = Field(default=UNSET, alias="accountHolderIds")
    """The unique identifiers of the account holders associated with the donation campaign."""

    in_person: OptionalNullable[InPersonDonationSettingsUpdate] = Field(default=UNSET, alias="inPerson")
    """The settings for in-person donations collected as part of the campaign."""

    name: Optional[str] = UNSET
    """The name of the donation campaign."""

    online: OptionalNullable[OnlineDonationSettingsUpdate] = UNSET
    """The settings for online donations collected as part of the campaign."""


class DonationCampaignUpdateDict(TypedDict):
    account_holder_ids: NotRequired[list[str | None]]
    in_person: NotRequired[InPersonDonationSettingsUpdate | InPersonDonationSettingsUpdateDict | None]
    name: NotRequired[str]
    online: NotRequired[OnlineDonationSettingsUpdate | OnlineDonationSettingsUpdateDict | None]
