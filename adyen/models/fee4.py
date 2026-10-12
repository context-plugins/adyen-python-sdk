from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .amount17 import Amount17, Amount17Dict


class Fee4(SdkBaseModel):
    """An object containing the fee currency and value, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__."""

    amount: Amount17
    """Contains the fee amount."""


class Fee4Dict(TypedDict):
    amount: Amount17Dict
