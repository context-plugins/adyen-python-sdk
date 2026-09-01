from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Amount42(SdkBaseModel):
    """For a billing plan where the payment amounts are variable, the minimum amount to charge the shopper for each
    recurring payment. When a shopper approves the billing plan, they can also specify a maximum amount in their banking
    app."""

    currency: str
    """The three-character `ISO currency code
    <https://docs.adyen.com/development-resources/currency-codes#currency-codes>`__ of the amount."""

    value: int
    """The numeric value of the amount, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes#minor-units>`__."""


class Amount42Dict(TypedDict):
    currency: str
    value: int
