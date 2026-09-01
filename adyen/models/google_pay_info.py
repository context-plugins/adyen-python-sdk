from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GooglePayInfo(SdkBaseModel):
    merchant_id: str = Field(alias="merchantId")
    """Google Pay `Merchant ID <https://support.google.com/paymentscenter/answer/7163092?hl=en>`__. Character length and
    limitations: 16 alphanumeric characters or 20 numeric characters."""

    reuse_merchant_id: Optional[bool] = Field(default=UNSET, alias="reuseMerchantId")
    """Indicates whether the Google Pay Merchant ID is used for several merchant accounts. Default value: **false**."""


class GooglePayInfoDict(TypedDict):
    merchant_id: str
    reuse_merchant_id: NotRequired[bool]
