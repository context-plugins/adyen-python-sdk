from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GooglePayResponseInfo(SdkBaseModel):
    merchant_id: Optional[str] = Field(default=UNSET, alias="merchantId")
    """Google Pay [Merchant ID]"""

    reuse_merchant_id: Optional[bool] = Field(default=UNSET, alias="reuseMerchantId")
    """Indicates whether the Google Pay Merchant ID is used for several merchant accounts."""


class GooglePayResponseInfoDict(TypedDict):
    merchant_id: NotRequired[str]
    reuse_merchant_id: NotRequired[bool]
