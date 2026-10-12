from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount17 import Amount17, Amount17Dict


class GrantLimit1(SdkBaseModel):
    amount: Optional[Amount17] = UNSET
    """The limit amount of the grant account."""


class GrantLimit1Dict(TypedDict):
    amount: NotRequired[Amount17Dict]
