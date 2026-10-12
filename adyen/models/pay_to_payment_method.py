from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PayToPaymentMethod(SdkBaseModel):
    """All Of ShopperIdPaymentMethod, PayToPaymentMethod."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    shopper_reference: Optional[str] = Field(default=UNSET, alias="shopperReference")


class PayToPaymentMethodDict(TypedDict):
    type_: NotRequired[str]
    shopper_reference: NotRequired[str]
