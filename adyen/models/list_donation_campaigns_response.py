from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .donation_campaign1 import DonationCampaign1, DonationCampaign1Dict
from .pagination_links1 import PaginationLinks1, PaginationLinks1Dict


class ListDonationCampaignsResponse(SdkBaseModel):
    links: Optional[PaginationLinks1] = Field(default=UNSET, alias="_links")
    """Pagination references."""

    campaigns: Optional[list[DonationCampaign1]] = UNSET
    """The list of donation campaigns."""

    items_total: int = Field(alias="itemsTotal")
    """Total number of items."""

    pages_total: int = Field(alias="pagesTotal")
    """Total number of pages."""


class ListDonationCampaignsResponseDict(TypedDict):
    links: NotRequired[PaginationLinks1Dict]
    campaigns: NotRequired[list[DonationCampaign1Dict]]
    items_total: int
    pages_total: int
