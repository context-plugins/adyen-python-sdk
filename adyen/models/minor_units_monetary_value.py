from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MinorUnitsMonetaryValue(SdkBaseModel):
    amount: Optional[int] = UNSET
    """The transaction amount, in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__."""

    currency_code: Optional[str] = Field(default=UNSET, alias="currencyCode")
    """The three-character `ISO currency code <https://docs.adyen.com/development-resources/currency-codes>`__."""


class MinorUnitsMonetaryValueDict(TypedDict):
    amount: NotRequired[int]
    currency_code: NotRequired[str]
