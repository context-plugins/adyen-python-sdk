from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AlipayPlusResponseInfo(SdkBaseModel):
    settlement_currency_code: Optional[str] = Field(default=UNSET, alias="settlementCurrencyCode")
    """The currency used for settlement."""


class AlipayPlusResponseInfoDict(TypedDict):
    settlement_currency_code: NotRequired[str]
