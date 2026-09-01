from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PayPalResponseInfo1(SdkBaseModel):
    """**paypal** details"""

    direct_capture: Optional[bool] = Field(default=UNSET, alias="directCapture")
    """Indicates if direct (immediate) capture for PayPal is enabled. If set to **true**, this setting overrides the
    `capture <https://docs.adyen.com/online-payments/capture>`__ settings of your merchant account. Default value:
    **true**."""

    payer_id: Optional[str] = Field(default=UNSET, alias="payerId")
    """PayPal Merchant ID. Character length and limitations: 13 single-byte alphanumeric characters."""

    subject: Optional[str] = UNSET
    """Your business email address."""


class PayPalResponseInfo1Dict(TypedDict):
    direct_capture: NotRequired[bool]
    payer_id: NotRequired[str]
    subject: NotRequired[str]
