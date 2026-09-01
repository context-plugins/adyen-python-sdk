from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ApplePayResponseInfo(SdkBaseModel):
    domains: Optional[list[str]] = UNSET
    """The list of merchant domains.

    For more information, see `Apple Pay documentation
    <https://docs.adyen.com/payment-methods/apple-pay/web-drop-in?tab=adyen-certificate-live_1#going-live>`__."""


class ApplePayResponseInfoDict(TypedDict):
    domains: NotRequired[list[str]]
