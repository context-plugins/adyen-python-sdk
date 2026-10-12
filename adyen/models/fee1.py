from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .amount17 import Amount17, Amount17Dict


class Fee1(SdkBaseModel):
    """Details of the fee configuration."""

    amount: Amount17
    """Contains the fee amount."""


class Fee1Dict(TypedDict):
    amount: Amount17Dict
