from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pagination_links1 import PaginationLinks1, PaginationLinks1Dict
from .webhook import Webhook, WebhookDict


class ListWebhooksResponse(SdkBaseModel):
    links: Optional[PaginationLinks1] = Field(default=UNSET, alias="_links")
    """Pagination references."""

    account_reference: Optional[str] = Field(default=UNSET, alias="accountReference")
    """Reference to the account."""

    data: Optional[list[Webhook]] = UNSET
    """The list of webhooks configured for this account."""

    items_total: int = Field(alias="itemsTotal")
    """Total number of items."""

    pages_total: int = Field(alias="pagesTotal")
    """Total number of pages."""


class ListWebhooksResponseDict(TypedDict):
    links: NotRequired[PaginationLinks1Dict]
    account_reference: NotRequired[str]
    data: NotRequired[list[WebhookDict]]
    items_total: int
    pages_total: int
