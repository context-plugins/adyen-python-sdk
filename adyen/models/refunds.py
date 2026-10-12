from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .referenced1 import Referenced1, Referenced1Dict
from .unreferenced2 import Unreferenced2, Unreferenced2Dict


class Refunds(SdkBaseModel):
    referenced: Optional[Referenced1] = UNSET
    """Settings for referenced refunds."""

    unreferenced: Optional[Unreferenced2] = UNSET
    """Settings for unreferenced refunds."""


class RefundsDict(TypedDict):
    referenced: NotRequired[Referenced1Dict]
    unreferenced: NotRequired[Unreferenced2Dict]
