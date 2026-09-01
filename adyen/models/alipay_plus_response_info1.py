from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AlipayPlusResponseInfo1(SdkBaseModel):
    """**alipay_plus** details"""

    settlement_currency_code: Optional[str] = Field(default=UNSET, alias="settlementCurrencyCode")
    """The currency used for settlement."""


class AlipayPlusResponseInfo1Dict(TypedDict):
    settlement_currency_code: NotRequired[str]
