from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pagination_links1 import PaginationLinks1, PaginationLinks1Dict
from .store import Store, StoreDict


class ListStoresResponse(SdkBaseModel):
    links: Optional[PaginationLinks1] = Field(default=UNSET, alias="_links")
    """Pagination references."""

    data: Optional[list[Store]] = UNSET
    """List of stores"""

    items_total: int = Field(alias="itemsTotal")
    """Total number of items."""

    pages_total: int = Field(alias="pagesTotal")
    """Total number of pages."""


class ListStoresResponseDict(TypedDict):
    links: NotRequired[PaginationLinks1 | PaginationLinks1Dict]
    data: NotRequired[list[Store | StoreDict]]
    items_total: int
    pages_total: int
