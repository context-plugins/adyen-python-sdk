from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .association_listing import AssociationListing, AssociationListingDict
from .link3 import Link3, Link3Dict


class ListAssociationsResponse(SdkBaseModel):
    links: Link3 = Field(alias="_links")
    """A list of hyperlinks to resources related to this response."""

    data: list[AssociationListing]
    """Contains a list of associations and their corresponding details."""

    items_total: int = Field(alias="itemsTotal")
    """The total number of items available."""

    pages_total: int = Field(alias="pagesTotal")
    """The total number of pages available."""


class ListAssociationsResponseDict(TypedDict):
    links: Link3Dict
    data: list[AssociationListingDict]
    items_total: int
    pages_total: int
