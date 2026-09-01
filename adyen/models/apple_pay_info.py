from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ApplePayInfo(SdkBaseModel):
    domains: list[str]
    """The list of merchant domains. Maximum: 99 domains per request.

    For more information, see `Apple Pay documentation
    <https://docs.adyen.com/payment-methods/apple-pay/web-drop-in?tab=adyen-certificate-live_1#going-live>`__."""


class ApplePayInfoDict(TypedDict):
    domains: list[str]
