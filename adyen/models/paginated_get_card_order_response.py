from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .card_order import CardOrder, CardOrderDict


class PaginatedGetCardOrderResponse(SdkBaseModel):
    card_orders: Optional[list[CardOrder]] = Field(default=UNSET, alias="cardOrders")
    """Contains objects with information about card orders."""

    has_next: bool = Field(alias="hasNext")
    """Indicates whether there are more items on the next page."""

    has_previous: bool = Field(alias="hasPrevious")
    """Indicates whether there are more items on the previous page."""


class PaginatedGetCardOrderResponseDict(TypedDict):
    card_orders: NotRequired[list[CardOrder | CardOrderDict]]
    has_next: bool
    has_previous: bool
