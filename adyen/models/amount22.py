from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Amount22(SdkBaseModel):
    """The currency of the amount you converted (the source amount)."""

    currency: str
    """The three-character `ISO currency code
    <https://docs.adyen.com/development-resources/currency-codes#currency-codes>`__."""

    value: int
    """The amount of the transaction, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes#minor-units>`__."""


class Amount22Dict(TypedDict):
    currency: str
    value: int
