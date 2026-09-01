from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PayPalInfo(SdkBaseModel):
    direct_capture: Optional[bool] = Field(default=UNSET, alias="directCapture")
    """Indicates if direct (immediate) capture for PayPal is enabled. If set to **true**, this setting overrides the
    `capture <https://docs.adyen.com/online-payments/capture>`__ settings of your merchant account. Default value:
    **true**."""

    payer_id: str = Field(alias="payerId")
    """PayPal Merchant ID. Character length and limitations: 13 single-byte alphanumeric characters."""

    subject: str
    """Your business email address."""


class PayPalInfoDict(TypedDict):
    direct_capture: NotRequired[bool]
    payer_id: str
    subject: str
