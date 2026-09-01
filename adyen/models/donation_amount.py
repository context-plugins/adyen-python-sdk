from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DonationAmount(SdkBaseModel):
    amounts: list[int]
    """The donation amounts in minor units. The list must contain at least one amount and no more than three amounts."""

    currency_code: str = Field(alias="currencyCode")
    """The three-character `ISO currency code
    <https://docs.adyen.com/development-resources/currency-codes#currency-codes>`__."""


class DonationAmountDict(TypedDict):
    amounts: list[int]
    currency_code: str
