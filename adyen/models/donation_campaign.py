from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amounts1 import Amounts1, Amounts1Dict
from .donation1 import Donation1, Donation1Dict


class DonationCampaign(SdkBaseModel):
    amounts: Optional[Amounts1] = UNSET
    """The object that contains the fixed donation amounts that the shopper can select from."""

    banner_url: Optional[str] = Field(default=UNSET, alias="bannerUrl")
    """The URL for the banner of the nonprofit or campaign."""

    campaign_name: Optional[str] = Field(default=UNSET, alias="campaignName")
    """The name of the donation campaign.."""

    cause_name: Optional[str] = Field(default=UNSET, alias="causeName")
    """The cause of the nonprofit."""

    donation: Optional[Donation1] = UNSET
    """The object that contains the details of the donation."""

    id: Optional[str] = UNSET
    """The unique campaign ID of the donation campaign."""

    logo_url: Optional[str] = Field(default=UNSET, alias="logoUrl")
    """The URL for the logo of the nonprofit."""

    nonprofit_description: Optional[str] = Field(default=UNSET, alias="nonprofitDescription")
    """The description of the nonprofit."""

    nonprofit_name: Optional[str] = Field(default=UNSET, alias="nonprofitName")
    """The name of the nonprofit organization that receives the donation."""

    nonprofit_url: Optional[str] = Field(default=UNSET, alias="nonprofitUrl")
    """The website URL of the nonprofit."""

    terms_and_conditions_url: Optional[str] = Field(default=UNSET, alias="termsAndConditionsUrl")
    """The URL of the terms and conditions page of the nonprofit and the campaign."""


class DonationCampaignDict(TypedDict):
    amounts: NotRequired[Amounts1 | Amounts1Dict]
    banner_url: NotRequired[str]
    campaign_name: NotRequired[str]
    cause_name: NotRequired[str]
    donation: NotRequired[Donation1 | Donation1Dict]
    id: NotRequired[str]
    logo_url: NotRequired[str]
    nonprofit_description: NotRequired[str]
    nonprofit_name: NotRequired[str]
    nonprofit_url: NotRequired[str]
    terms_and_conditions_url: NotRequired[str]
