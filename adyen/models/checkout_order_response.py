from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount12 import Amount12, Amount12Dict
from .amount13 import Amount13, Amount13Dict


class CheckoutOrderResponse(SdkBaseModel):
    amount: Optional[Amount12] = UNSET
    """The initial amount of the order."""

    expires_at: Optional[str] = Field(default=UNSET, alias="expiresAt")
    """The expiry date for the order."""

    order_data: Optional[str] = Field(default=UNSET, alias="orderData")
    """The encrypted order data."""

    psp_reference: str = Field(alias="pspReference")
    """The ``pspReference`` that belongs to the order."""

    reference: Optional[str] = UNSET
    """The merchant reference for the order."""

    remaining_amount: Optional[Amount13] = Field(default=UNSET, alias="remainingAmount")
    """The updated remaining amount."""


class CheckoutOrderResponseDict(TypedDict):
    amount: NotRequired[Amount12Dict]
    expires_at: NotRequired[str]
    order_data: NotRequired[str]
    psp_reference: str
    reference: NotRequired[str]
    remaining_amount: NotRequired[Amount13Dict]
