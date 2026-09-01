from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .nonprofit import Nonprofit, NonprofitDict
from .pagination_links1 import PaginationLinks1, PaginationLinks1Dict


class ListNonprofitsResponse(SdkBaseModel):
    links: Optional[PaginationLinks1] = Field(default=UNSET, alias="_links")
    """Pagination references."""

    items_total: int = Field(alias="itemsTotal")
    """Total number of items."""

    nonprofits: Optional[list[Nonprofit]] = UNSET
    """The supported nonprofit organizations."""

    pages_total: int = Field(alias="pagesTotal")
    """Total number of pages."""


class ListNonprofitsResponseDict(TypedDict):
    links: NotRequired[PaginationLinks1 | PaginationLinks1Dict]
    items_total: int
    nonprofits: NotRequired[list[Nonprofit | NonprofitDict]]
    pages_total: int
