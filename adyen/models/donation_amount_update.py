from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DonationAmountUpdate(SdkBaseModel):
    amounts: Optional[list[int]] = UNSET
    """The donation amounts in minor units. The list must contain at least one amount and no more than three amounts."""

    currency_code: Optional[str] = Field(default=UNSET, alias="currencyCode")
    """The three-character `ISO currency code
    <https://docs.adyen.com/development-resources/currency-codes#currency-codes>`__."""


class DonationAmountUpdateDict(TypedDict):
    amounts: NotRequired[list[int]]
    currency_code: NotRequired[str]
