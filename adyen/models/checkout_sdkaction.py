from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type19 import Type19OrStr


class CheckoutSdkaction(SdkBaseModel):
    payment_data: Optional[str] = Field(default=UNSET, alias="paymentData")
    """Encoded payment data."""

    payment_method_type: Optional[str] = Field(default=UNSET, alias="paymentMethodType")
    """Specifies the payment method."""

    sdk_data: Optional[dict[str, str]] = Field(default=UNSET, alias="sdkData")
    """The data to pass to the SDK."""

    type_: Type19OrStr = Field(alias="type")
    """The type of the action."""

    url: Optional[str] = UNSET
    """Specifies the URL to redirect to."""


class CheckoutSdkactionDict(TypedDict):
    payment_data: NotRequired[str]
    payment_method_type: NotRequired[str]
    sdk_data: NotRequired[dict[str, str]]
    type_: Type19OrStr
    url: NotRequired[str]
