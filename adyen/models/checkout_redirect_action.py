from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CheckoutRedirectAction(SdkBaseModel):
    data: Optional[dict[str, str]] = UNSET
    """When the redirect URL must be accessed via POST, use this data to post to the redirect URL."""

    method: Optional[str] = UNSET
    """Specifies the HTTP method, for example GET or POST."""

    payment_method_type: Optional[str] = Field(default=UNSET, alias="paymentMethodType")
    """Specifies the payment method."""

    type_: Literal["redirect"] = Field(default="redirect", alias="type")
    """**redirect**"""

    url: Optional[str] = UNSET
    """Specifies the URL to redirect to."""


class CheckoutRedirectActionDict(TypedDict):
    data: NotRequired[dict[str, str]]
    method: NotRequired[str]
    payment_method_type: NotRequired[str]
    type_: Literal["redirect"]
    url: NotRequired[str]
