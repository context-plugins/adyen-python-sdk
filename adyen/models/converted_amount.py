from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ConvertedAmount(SdkBaseModel):
    amount_value: float = Field(alias="AmountValue")
    """Value of an amount."""

    currency: str = Field(alias="Currency")
    """Currency of a monetary amount."""


class ConvertedAmountDict(TypedDict):
    amount_value: float
    currency: str
