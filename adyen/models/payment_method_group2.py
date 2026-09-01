from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PaymentMethodGroup2(SdkBaseModel):
    """The group where this payment method belongs to."""

    name: Optional[str] = UNSET
    """The name of the group."""

    payment_method_data: Optional[str] = Field(default=UNSET, alias="paymentMethodData")
    """Echo data to be used if the payment method is displayed as part of this group."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The unique code of the group."""


class PaymentMethodGroup2Dict(TypedDict):
    name: NotRequired[str]
    payment_method_data: NotRequired[str]
    type_: NotRequired[str]
