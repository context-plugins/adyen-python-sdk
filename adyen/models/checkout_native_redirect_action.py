from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CheckoutNativeRedirectAction(SdkBaseModel):
    data: Optional[dict[str, str]] = UNSET
    """When the redirect URL must be accessed via POST, use this data to post to the redirect URL."""

    method: Optional[str] = UNSET
    """Specifies the HTTP method, for example GET or POST."""

    native_redirect_data: Optional[str] = Field(default=UNSET, alias="nativeRedirectData")
    """Native SDK's redirect data containing the direct issuer link and state data that must be submitted to the
    /v1/nativeRedirect/redirectResult."""

    payment_method_type: Optional[str] = Field(default=UNSET, alias="paymentMethodType")
    """Specifies the payment method."""

    type_: Literal["nativeRedirect"] = Field(default="nativeRedirect", alias="type")
    """**nativeRedirect**"""

    url: Optional[str] = UNSET
    """Specifies the URL to redirect to."""


class CheckoutNativeRedirectActionDict(TypedDict):
    data: NotRequired[dict[str, str]]
    method: NotRequired[str]
    native_redirect_data: NotRequired[str]
    payment_method_type: NotRequired[str]
    type_: NotRequired[Literal["nativeRedirect"]]
    url: NotRequired[str]
