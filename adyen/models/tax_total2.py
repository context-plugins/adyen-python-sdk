from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount import Amount, AmountDict


class TaxTotal2(SdkBaseModel):
    """Total tax amount from the order."""

    amount: Optional[Amount] = UNSET


class TaxTotal2Dict(TypedDict):
    amount: NotRequired[Amount | AmountDict]
