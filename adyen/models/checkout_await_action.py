from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CheckoutAwaitAction(SdkBaseModel):
    payment_data: Optional[str] = Field(default=UNSET, alias="paymentData")
    """Encoded payment data."""

    payment_method_type: Optional[str] = Field(default=UNSET, alias="paymentMethodType")
    """Specifies the payment method."""

    type_: Literal["await"] = Field(default="await", alias="type")
    """**await**"""

    url: Optional[str] = UNSET
    """Specifies the URL to redirect to."""


class CheckoutAwaitActionDict(TypedDict):
    payment_data: NotRequired[str]
    payment_method_type: NotRequired[str]
    type_: Literal["await"]
    url: NotRequired[str]
