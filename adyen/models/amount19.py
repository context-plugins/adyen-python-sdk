from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Amount19(SdkBaseModel):
    """An object specifying the currency and value for which you want to perform an exchange calculation."""

    currency: str
    """The three-character `ISO currency code
    <https://docs.adyen.com/development-resources/currency-codes#currency-codes>`__."""

    value: int
    """The amount of the transaction, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes#minor-units>`__."""


class Amount19Dict(TypedDict):
    currency: str
    value: int
