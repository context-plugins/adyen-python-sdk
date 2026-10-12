from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .company_api_credential import CompanyApiCredential, CompanyApiCredentialDict
from .pagination_links1 import PaginationLinks1, PaginationLinks1Dict


class ListCompanyApiCredentialsResponse(SdkBaseModel):
    links: Optional[PaginationLinks1] = Field(default=UNSET, alias="_links")
    """Pagination references."""

    data: Optional[list[CompanyApiCredential]] = UNSET
    """The list of API credentials."""

    items_total: int = Field(alias="itemsTotal")
    """Total number of items."""

    pages_total: int = Field(alias="pagesTotal")
    """Total number of pages."""


class ListCompanyApiCredentialsResponseDict(TypedDict):
    links: NotRequired[PaginationLinks1Dict]
    data: NotRequired[list[CompanyApiCredentialDict]]
    items_total: int
    pages_total: int
