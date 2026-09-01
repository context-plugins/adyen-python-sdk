from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .amount17 import Amount17, Amount17Dict


class Fee21(SdkBaseModel):
    """Contains the currency and value of the cashout fee, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__."""

    amount: Amount17
    """Contains the fee amount."""


class Fee21Dict(TypedDict):
    amount: Amount17 | Amount17Dict
