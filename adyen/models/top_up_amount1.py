from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount17 import Amount17, Amount17Dict


class TopUpAmount1(SdkBaseModel):
    """The currency and value to be added to the balance account, specified in minor units. This can be a fixed amount
    or a target amount."""

    fixed: Optional[Amount17] = UNSET
    """The fixed amount with which you want to top up the balance account."""

    target: Optional[Amount17] = UNSET
    """The target balance for the balance account that the top-up must achieve."""


class TopUpAmount1Dict(TypedDict):
    fixed: NotRequired[Amount17Dict]
    target: NotRequired[Amount17Dict]
