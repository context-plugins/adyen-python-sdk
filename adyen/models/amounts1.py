from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Amounts1(SdkBaseModel):
    """The object that contains the fixed donation amounts that the shopper can select from."""

    currency: str
    """The three-character `ISO currency code <https://docs.adyen.com/development-resources/currency-codes/>`__."""

    values: list[int]
    """The amounts of the donation (in `minor units
    <https://docs.adyen.com/development-resources/currency-codes/>`__)."""


class Amounts1Dict(TypedDict):
    currency: str
    values: list[int]
