from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .company2 import Company2, Company2Dict
from .pagination_links1 import PaginationLinks1, PaginationLinks1Dict


class ListCompanyResponse(SdkBaseModel):
    links: Optional[PaginationLinks1] = Field(default=UNSET, alias="_links")
    """Pagination references."""

    data: Optional[list[Company2]] = UNSET
    """The list of companies."""

    items_total: int = Field(alias="itemsTotal")
    """Total number of items."""

    pages_total: int = Field(alias="pagesTotal")
    """Total number of pages."""


class ListCompanyResponseDict(TypedDict):
    links: NotRequired[PaginationLinks1 | PaginationLinks1Dict]
    data: NotRequired[list[Company2 | Company2Dict]]
    items_total: int
    pages_total: int
