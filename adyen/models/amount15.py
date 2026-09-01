from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Amount15(SdkBaseModel):
    """The surcharge amount."""

    currency: str
    """The three-character `ISO currency code
    <https://docs.adyen.com/development-resources/currency-codes#currency-codes>`__ of the amount."""

    value: int
    """The numeric value of the amount, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes#minor-units>`__."""


class Amount15Dict(TypedDict):
    currency: str
    value: int
