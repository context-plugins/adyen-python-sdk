from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .calculate_rate_request_item import CalculateRateRequestItem, CalculateRateRequestItemDict


class CalculateRateRequest(SdkBaseModel):
    """The request to calculate an amount in a different currency."""

    exchange_calculations: list[CalculateRateRequestItem] = Field(alias="exchangeCalculations")
    """An array of objects, where each object defines a currency and value for which you want to perform an exchange
    calculation."""


class CalculateRateRequestDict(TypedDict):
    exchange_calculations: list[CalculateRateRequestItemDict]
