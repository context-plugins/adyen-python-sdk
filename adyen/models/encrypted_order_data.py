from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EncryptedOrderData(SdkBaseModel):
    order_data: str = Field(alias="orderData")
    """The encrypted order data."""

    psp_reference: str = Field(alias="pspReference")
    """The ``pspReference`` that belongs to the order."""


class EncryptedOrderDataDict(TypedDict):
    order_data: str
    psp_reference: str
