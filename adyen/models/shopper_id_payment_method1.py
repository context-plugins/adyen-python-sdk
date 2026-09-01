from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ShopperIdPaymentMethod1(SdkBaseModel):
    """paymentMethod"""

    type_: Optional[str] = Field(default=UNSET, alias="type")


class ShopperIdPaymentMethod1Dict(TypedDict):
    type_: NotRequired[str]
