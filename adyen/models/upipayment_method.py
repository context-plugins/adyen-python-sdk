from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UpipaymentMethod(SdkBaseModel):
    """All Of ShopperIdPaymentMethod, UPIPaymentMethod."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    virtual_payment_address: Optional[str] = Field(default=UNSET, alias="virtualPaymentAddress")


class UpipaymentMethodDict(TypedDict):
    type_: NotRequired[str]
    virtual_payment_address: NotRequired[str]
