from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .card_order_item import CardOrderItem, CardOrderItemDict


class PaginatedGetCardOrderItemResponse(SdkBaseModel):
    data: list[CardOrderItem]
    """List of card order items in the card order batch."""

    has_next: bool = Field(alias="hasNext")
    """Indicates whether there are more items on the next page."""

    has_previous: bool = Field(alias="hasPrevious")
    """Indicates whether there are more items on the previous page."""


class PaginatedGetCardOrderItemResponseDict(TypedDict):
    data: list[CardOrderItemDict]
    has_next: bool
    has_previous: bool
