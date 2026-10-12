from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount import Amount, AmountDict


class TaxTotal(SdkBaseModel):
    amount: Optional[Amount] = UNSET


class TaxTotalDict(TypedDict):
    amount: NotRequired[AmountDict]
