from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PayToPaymentMethod(SdkBaseModel):
    """All Of ShopperIdPaymentMethod, PayToPaymentMethod."""

    type_: Literal["payTo"] = Field(default="payTo", alias="type")

    shopper_reference: Optional[str] = Field(default=UNSET, alias="shopperReference")


class PayToPaymentMethodDict(TypedDict):
    type_: NotRequired[Literal["payTo"]]
    shopper_reference: NotRequired[str]
