from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .donation_campaign import DonationCampaign, DonationCampaignDict


class DonationCampaignsResponse(SdkBaseModel):
    donation_campaigns: Optional[list[DonationCampaign]] = Field(default=UNSET, alias="donationCampaigns")
    """List of active donation campaigns for your merchant account."""


class DonationCampaignsResponseDict(TypedDict):
    donation_campaigns: NotRequired[list[DonationCampaignDict]]
