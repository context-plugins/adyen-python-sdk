from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Amount1(SdkBaseModel):
    """If you want a `BIN or card verification
    <https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification>`__ request to use a non-zero value,
    assign this value to ``additionalAmount`` (while the amount must be still set to 0 to trigger BIN or card
    verification). Required to be in the same currency as the ``amount``."""

    currency: str
    """The three-character `ISO currency code
    <https://docs.adyen.com/development-resources/currency-codes#currency-codes>`__ of the amount."""

    value: int
    """The numeric value of the amount, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes#minor-units>`__."""


class Amount1Dict(TypedDict):
    currency: str
    value: int
