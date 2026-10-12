from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .amount17 import Amount17, Amount17Dict


class Fee(SdkBaseModel):
    amount: Amount17
    """Contains the fee amount."""


class FeeDict(TypedDict):
    amount: Amount17Dict
