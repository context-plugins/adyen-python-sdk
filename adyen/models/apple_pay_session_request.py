from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ApplePaySessionRequest(SdkBaseModel):
    display_name: str = Field(alias="displayName")
    """This is the name that your shoppers will see in the Apple Pay interface.

    The value returned as ``configuration.merchantName`` field from the
    https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/paymentMethods response."""

    domain_name: str = Field(alias="domainName")
    """The domain name you provided when you added Apple Pay in your Customer Area.

    This must match the ``window.location.hostname`` of the web shop."""

    merchant_identifier: str = Field(alias="merchantIdentifier")
    """Your merchant identifier registered with Apple Pay.

    Use the value of the ``configuration.merchantId`` field from the
    https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/paymentMethods response."""


class ApplePaySessionRequestDict(TypedDict):
    display_name: str
    domain_name: str
    merchant_identifier: str
