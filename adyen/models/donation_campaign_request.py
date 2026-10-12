from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .in_person_donation_settings2 import InPersonDonationSettings2, InPersonDonationSettings2Dict
from .online_donation_settings2 import OnlineDonationSettings2, OnlineDonationSettings2Dict


class DonationCampaignRequest(SdkBaseModel):
    account_holder_ids: Optional[list[str]] = Field(default=UNSET, alias="accountHolderIds")
    """The unique identifiers of the account holders associated with the donation campaign."""

    in_person: Optional[InPersonDonationSettings2] = Field(default=UNSET, alias="inPerson")
    """The settings for in-person donations collected as part of the campaign."""

    name: str
    """The name of the donation campaign."""

    nonprofit_cause_id: str = Field(alias="nonprofitCauseId")
    """The unique identifier of the nonprofit cause that the campaign supports."""

    online: Optional[OnlineDonationSettings2] = UNSET
    """The settings for online donations collected as part of the campaign."""


class DonationCampaignRequestDict(TypedDict):
    account_holder_ids: NotRequired[list[str]]
    in_person: NotRequired[InPersonDonationSettings2Dict]
    name: str
    nonprofit_cause_id: str
    online: NotRequired[OnlineDonationSettings2Dict]
