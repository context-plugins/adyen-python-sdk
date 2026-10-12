from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .amount17 import Amount17, Amount17Dict


class ThresholdRepayment(SdkBaseModel):
    amount: Amount17
    """The amount to be repaid on a 30-day basis."""


class ThresholdRepaymentDict(TypedDict):
    amount: Amount17Dict
