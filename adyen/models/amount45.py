from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Amount45(SdkBaseModel):
    """The discount amount for this order."""

    currency: str
    """The three-character `ISO currency code
    <https://docs.adyen.com/development-resources/currency-codes#currency-codes>`__ of the amount."""

    value: int
    """The numeric value of the amount, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes#minor-units>`__."""


class Amount45Dict(TypedDict):
    currency: str
    value: int
