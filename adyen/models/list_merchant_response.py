from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .merchant import Merchant, MerchantDict
from .pagination_links1 import PaginationLinks1, PaginationLinks1Dict


class ListMerchantResponse(SdkBaseModel):
    links: Optional[PaginationLinks1] = Field(default=UNSET, alias="_links")
    """Pagination references."""

    data: Optional[list[Merchant]] = UNSET
    """The list of merchant accounts."""

    items_total: int = Field(alias="itemsTotal")
    """Total number of items."""

    pages_total: int = Field(alias="pagesTotal")
    """Total number of pages."""


class ListMerchantResponseDict(TypedDict):
    links: NotRequired[PaginationLinks1 | PaginationLinks1Dict]
    data: NotRequired[list[Merchant | MerchantDict]]
    items_total: int
    pages_total: int
