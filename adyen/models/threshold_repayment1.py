from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .amount17 import Amount17, Amount17Dict


class ThresholdRepayment1(SdkBaseModel):
    amount: Amount17
    """The minimum threshold amount that your user must repay on every 30-day period."""


class ThresholdRepayment1Dict(TypedDict):
    amount: Amount17 | Amount17Dict
