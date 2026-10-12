from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .api_credential import ApiCredential, ApiCredentialDict
from .pagination_links1 import PaginationLinks1, PaginationLinks1Dict


class ListMerchantApiCredentialsResponse(SdkBaseModel):
    links: Optional[PaginationLinks1] = Field(default=UNSET, alias="_links")
    """Pagination references."""

    data: Optional[list[ApiCredential]] = UNSET
    """The list of API credentials."""

    items_total: int = Field(alias="itemsTotal")
    """Total number of items."""

    pages_total: int = Field(alias="pagesTotal")
    """Total number of pages."""


class ListMerchantApiCredentialsResponseDict(TypedDict):
    links: NotRequired[PaginationLinks1Dict]
    data: NotRequired[list[ApiCredentialDict]]
    items_total: int
    pages_total: int
