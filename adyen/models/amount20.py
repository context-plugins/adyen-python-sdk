from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Amount20(SdkBaseModel):
    currency: str
    """The three-character `ISO 4217 currency code
    <https://docs.adyen.com/development-resources/currency-codes#currency-codes>`__."""

    value: int
    """The amount of the transaction in `minor units
    <https://docs.adyen.com/development-resources/currency-codes#minor-units>`__ (cents)."""


class Amount20Dict(TypedDict):
    currency: str
    value: int
