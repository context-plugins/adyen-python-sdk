from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ApplePaySessionResponse(SdkBaseModel):
    data: str
    """Base64 encoded data you need to `complete the Apple Pay merchant validation
    <https://docs.adyen.com/payment-methods/apple-pay/api-only?tab=adyen-certificate-validation_1#complete-apple-pay-session-validation>`__."""


class ApplePaySessionResponseDict(TypedDict):
    data: str
