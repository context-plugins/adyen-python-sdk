from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UpipaymentMethod(SdkBaseModel):
    """All Of ShopperIdPaymentMethod, UPIPaymentMethod."""

    type_: Literal["upi_collect"] = Field(default="upi_collect", alias="type")

    virtual_payment_address: Optional[str] = Field(default=UNSET, alias="virtualPaymentAddress")


class UpipaymentMethodDict(TypedDict):
    type_: NotRequired[Literal["upi_collect"]]
    virtual_payment_address: NotRequired[str]
