from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .encrypted_order_data4 import EncryptedOrderData4, EncryptedOrderData4Dict


class CancelOrderRequest(SdkBaseModel):
    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier that orderData belongs to."""

    order: EncryptedOrderData4
    """The order request object that contains a pspReference that represents the order and the matching encrypted order
    data."""


class CancelOrderRequestDict(TypedDict):
    merchant_account: str
    order: EncryptedOrderData4Dict
