from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Currency(SdkBaseModel):
    amount: Optional[int] = UNSET
    """Surcharge amount per transaction, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__."""

    currency_code: str = Field(alias="currencyCode")
    """Three-character `ISO currency code <https://docs.adyen.com/development-resources/currency-codes>`__. For example,
    **AUD**."""

    max_amount: Optional[int] = Field(default=UNSET, alias="maxAmount")
    """The maximum surcharge amount per transaction, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__."""

    percentage: Optional[float] = UNSET
    """Surcharge percentage per transaction. The maximum number of decimal places is two. For example, **1%** or
    **2.27%**."""


class CurrencyDict(TypedDict):
    amount: NotRequired[int]
    currency_code: str
    max_amount: NotRequired[int]
    percentage: NotRequired[float]
