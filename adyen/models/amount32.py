from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Amount32(SdkBaseModel):
    """Required for transactions performed by registered payment facilitators. The amount of the payment corresponding
    to each sub-merchant. This value will be different than the request amount if shopper is purchasing items at
    different sub-merchants' shops."""

    currency: str
    """The three-character `ISO currency code
    <https://docs.adyen.com/development-resources/currency-codes#currency-codes>`__ of the amount."""

    value: int
    """The numeric value of the amount, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes#minor-units>`__."""


class Amount32Dict(TypedDict):
    currency: str
    value: int
