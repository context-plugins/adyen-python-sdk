from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .amount17 import Amount17, Amount17Dict


class ThresholdRepayment21(SdkBaseModel):
    """Contains the minimum threshold amount that your user must repay every 30-day period."""

    amount: Amount17
    """The minimum threshold amount that your user must repay on every 30-day period."""


class ThresholdRepayment21Dict(TypedDict):
    amount: Amount17 | Amount17Dict
