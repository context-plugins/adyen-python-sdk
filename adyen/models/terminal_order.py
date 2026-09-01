from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .billing_entity1 import BillingEntity1, BillingEntity1Dict
from .order_item import OrderItem, OrderItemDict
from .shipping_location1 import ShippingLocation1, ShippingLocation1Dict


class TerminalOrder(SdkBaseModel):
    billing_entity: Optional[BillingEntity1] = Field(default=UNSET, alias="billingEntity")
    """The details of the entity that the order is billed to."""

    customer_order_reference: Optional[str] = Field(default=UNSET, alias="customerOrderReference")
    """The merchant-defined purchase order number. This will be printed on the packing list."""

    id: Optional[str] = UNSET
    """The unique identifier of the order."""

    items: Optional[list[OrderItem]] = UNSET
    """The products included in the order."""

    order_date: Optional[str] = Field(default=UNSET, alias="orderDate")
    """The date and time that the order was placed, in UTC ISO 8601 format. For example, "2011-12-03T10:15:30Z"."""

    shipping_location: Optional[ShippingLocation1] = Field(default=UNSET, alias="shippingLocation")
    """The details of the location where the order is shipped to."""

    status: Optional[str] = UNSET
    """The processing status of the order."""

    tracking_url: Optional[str] = Field(default=UNSET, alias="trackingUrl")
    """The URL, provided by the carrier company, where the shipment can be tracked."""


class TerminalOrderDict(TypedDict):
    billing_entity: NotRequired[BillingEntity1 | BillingEntity1Dict]
    customer_order_reference: NotRequired[str]
    id: NotRequired[str]
    items: NotRequired[list[OrderItem | OrderItemDict]]
    order_date: NotRequired[str]
    shipping_location: NotRequired[ShippingLocation1 | ShippingLocation1Dict]
    status: NotRequired[str]
    tracking_url: NotRequired[str]
