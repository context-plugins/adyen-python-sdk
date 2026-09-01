from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .card_order_item_delivery_status1 import CardOrderItemDeliveryStatus1, CardOrderItemDeliveryStatus1Dict
from .card_order_item_delivery_status3 import CardOrderItemDeliveryStatus3, CardOrderItemDeliveryStatus3Dict


class CardOrderItem(SdkBaseModel):
    balance_platform: Optional[str] = Field(default=UNSET, alias="balancePlatform")
    """The unique identifier of the balance platform."""

    card: Optional[CardOrderItemDeliveryStatus3] = UNSET
    """The status of the card delivery.

    Possible values: **created**, **rejected**, **processing**, **produced**, **shipped**, **delivered**,
    **notApplicable**, **unknown**."""

    card_order_item_id: Optional[str] = Field(default=UNSET, alias="cardOrderItemId")
    """The unique identifier of the card order item."""

    creation_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="creationDate")
    """The date and time when the event was triggered, in ISO 8601 extended format. For example,
    **2025-03-19T10:15:30+01:00**."""

    id: Optional[str] = UNSET
    """The ID of the resource."""

    payment_instrument_id: Optional[str] = Field(default=UNSET, alias="paymentInstrumentId")
    """The unique identifier of the payment instrument related to the card order item."""

    pin: Optional[CardOrderItemDeliveryStatus1] = UNSET
    """Contains information about the status of the PIN delivery."""

    shipping_method: Optional[str] = Field(default=UNSET, alias="shippingMethod")
    """The shipping method used to deliver the card or the PIN."""


class CardOrderItemDict(TypedDict):
    balance_platform: NotRequired[str]
    card: NotRequired[CardOrderItemDeliveryStatus3 | CardOrderItemDeliveryStatus3Dict]
    card_order_item_id: NotRequired[str]
    creation_date: NotRequired[RFC3339DateTime]
    id: NotRequired[str]
    payment_instrument_id: NotRequired[str]
    pin: NotRequired[CardOrderItemDeliveryStatus1 | CardOrderItemDeliveryStatus1Dict]
    shipping_method: NotRequired[str]
