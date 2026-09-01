from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ConvertedAmount1(SdkBaseModel):
    """Amount after a currency conversion."""

    amount_value: float = Field(alias="AmountValue")
    """Value of an amount."""

    currency: str = Field(alias="Currency")
    """Currency of a monetary amount."""


class ConvertedAmount1Dict(TypedDict):
    amount_value: float
    currency: str
