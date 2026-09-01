from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Amount44(SdkBaseModel):
    """The updated final payment amount. This amount is the item total plus the shipping costs of the selected
    ``deliveryMethod``."""

    currency: str
    """The three-character `ISO currency code
    <https://docs.adyen.com/development-resources/currency-codes#currency-codes>`__ of the amount."""

    value: int
    """The numeric value of the amount, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes#minor-units>`__."""


class Amount44Dict(TypedDict):
    currency: str
    value: int
