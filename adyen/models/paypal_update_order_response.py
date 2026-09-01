from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.status4 import Status4OrStr


class PaypalUpdateOrderResponse(SdkBaseModel):
    payment_data: str = Field(alias="paymentData")
    """The updated paymentData."""

    status: Status4OrStr
    """The status of the request. This indicates whether the order was successfully updated with PayPal."""


class PaypalUpdateOrderResponseDict(TypedDict):
    payment_data: str
    status: Status4OrStr
