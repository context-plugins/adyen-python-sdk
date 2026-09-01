from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .order_item import OrderItem, OrderItemDict


class TerminalOrderRequest(SdkBaseModel):
    billing_entity_id: Optional[str] = Field(default=UNSET, alias="billingEntityId")
    """The identification of the billing entity to use for the order.

     > When ordering products in Brazil, you do not need to include the ``billingEntityId`` in the request."""

    customer_order_reference: Optional[str] = Field(default=UNSET, alias="customerOrderReference")
    """The merchant-defined purchase order reference."""

    items: Optional[list[OrderItem]] = UNSET
    """The products included in the order."""

    order_type: Optional[str] = Field(default=UNSET, alias="orderType")
    """Type of order"""

    shipping_location_id: Optional[str] = Field(default=UNSET, alias="shippingLocationId")
    """The identification of the shipping location to use for the order."""

    tax_id: Optional[str] = Field(default=UNSET, alias="taxId")
    """The tax number of the billing entity."""


class TerminalOrderRequestDict(TypedDict):
    billing_entity_id: NotRequired[str]
    customer_order_reference: NotRequired[str]
    items: NotRequired[list[OrderItem | OrderItemDict]]
    order_type: NotRequired[str]
    shipping_location_id: NotRequired[str]
    tax_id: NotRequired[str]
