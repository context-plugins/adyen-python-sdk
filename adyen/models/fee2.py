from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .amount17 import Amount17, Amount17Dict


class Fee2(SdkBaseModel):
    amount: Amount17
    """Contains the amount of the grant fee."""


class Fee2Dict(TypedDict):
    amount: Amount17Dict
