from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount17 import Amount17, Amount17Dict


class TopUpAmount(SdkBaseModel):
    fixed: Optional[Amount17] = UNSET
    """The fixed amount with which you want to top up the balance account."""

    target: Optional[Amount17] = UNSET
    """The target balance for the balance account that the top-up must achieve."""


class TopUpAmountDict(TypedDict):
    fixed: NotRequired[Amount17Dict]
    target: NotRequired[Amount17Dict]
