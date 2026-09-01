from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Amount2(SdkBaseModel):
    """The amount information for the transaction (in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__). For `BIN or card verification
    <https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification>`__ requests, set amount to 0
    (zero)."""

    currency: str
    """The three-character `ISO currency code
    <https://docs.adyen.com/development-resources/currency-codes#currency-codes>`__ of the amount."""

    value: int
    """The numeric value of the amount, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes#minor-units>`__."""


class Amount2Dict(TypedDict):
    currency: str
    value: int
