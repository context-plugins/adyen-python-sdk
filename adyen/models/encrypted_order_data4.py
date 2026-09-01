from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EncryptedOrderData4(SdkBaseModel):
    """The order request object that contains a pspReference that represents the order and the matching encrypted order
    data."""

    order_data: str = Field(alias="orderData")
    """The encrypted order data."""

    psp_reference: str = Field(alias="pspReference")
    """The ``pspReference`` that belongs to the order."""


class EncryptedOrderData4Dict(TypedDict):
    order_data: str
    psp_reference: str
