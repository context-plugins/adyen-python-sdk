from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EncryptedOrderData2(SdkBaseModel):
    """The order information required for partial payments."""

    order_data: str = Field(alias="orderData")
    """The encrypted order data."""

    psp_reference: str = Field(alias="pspReference")
    """The ``pspReference`` that belongs to the order."""


class EncryptedOrderData2Dict(TypedDict):
    order_data: str
    psp_reference: str
