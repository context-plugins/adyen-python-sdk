from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount17 import Amount17, Amount17Dict


class GrantLimit(SdkBaseModel):
    amount: Optional[Amount17] = UNSET
    """The amount available on the grant account."""


class GrantLimitDict(TypedDict):
    amount: NotRequired[Amount17Dict]
