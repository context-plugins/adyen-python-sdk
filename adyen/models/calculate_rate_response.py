from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .calculate_rate_response_item import CalculateRateResponseItem, CalculateRateResponseItemDict


class CalculateRateResponse(SdkBaseModel):
    """The response returned when you calculate an amount in a different currency."""

    exchange_calculations: Optional[list[CalculateRateResponseItem]] = Field(
        default=UNSET, alias="exchangeCalculations"
    )
    """An array of objects, where each object returns a currency and value for which you performed an exchange
    calculation. You can use the calculated amounts in your payment requests."""


class CalculateRateResponseDict(TypedDict):
    exchange_calculations: NotRequired[list[CalculateRateResponseItem | CalculateRateResponseItemDict]]
