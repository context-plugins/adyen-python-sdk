from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .company_user import CompanyUser, CompanyUserDict
from .pagination_links1 import PaginationLinks1, PaginationLinks1Dict


class ListCompanyUsersResponse(SdkBaseModel):
    links: Optional[PaginationLinks1] = Field(default=UNSET, alias="_links")
    """Pagination references."""

    data: Optional[list[CompanyUser]] = UNSET
    """The list of users."""

    items_total: int = Field(alias="itemsTotal")
    """Total number of items."""

    pages_total: int = Field(alias="pagesTotal")
    """Total number of pages."""


class ListCompanyUsersResponseDict(TypedDict):
    links: NotRequired[PaginationLinks1Dict]
    data: NotRequired[list[CompanyUserDict]]
    items_total: int
    pages_total: int
