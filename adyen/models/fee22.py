from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .amount17 import Amount17, Amount17Dict


class Fee22(SdkBaseModel):
    """Contains information about the fee that your user must pay for the disbursement."""

    amount: Amount17
    """Contains the amount of the grant fee."""


class Fee22Dict(TypedDict):
    amount: Amount17Dict
