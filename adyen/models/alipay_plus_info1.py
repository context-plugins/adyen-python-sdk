from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AlipayPlusInfo1(SdkBaseModel):
    """Details to provide if ``type`` is **alipay_plus**."""

    settlement_currency_code: Optional[str] = Field(default=UNSET, alias="settlementCurrencyCode")
    """The currency used for settlement. Defaults to USD."""


class AlipayPlusInfo1Dict(TypedDict):
    settlement_currency_code: NotRequired[str]
