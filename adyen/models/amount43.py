from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Amount43(SdkBaseModel):
    """For a billing plan where the payment amount is fixed, the amount the shopper will be charged for each recurring
    payment."""

    currency: str
    """The three-character `ISO currency code
    <https://docs.adyen.com/development-resources/currency-codes#currency-codes>`__ of the amount."""

    value: int
    """The numeric value of the amount, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes#minor-units>`__."""


class Amount43Dict(TypedDict):
    currency: str
    value: int
