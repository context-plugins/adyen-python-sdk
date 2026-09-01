from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount17 import Amount17, Amount17Dict
from .schedule21 import Schedule21, Schedule21Dict


class Trigger1(SdkBaseModel):
    """The condition that triggers the top-up. This can be a recurring schedule or a minimum balance threshold."""

    schedule: Optional[Schedule21] = UNSET
    """Contains the details about the schedule that determines when the top up is executed."""

    threshold: Amount17
    """The balance threshold that triggers the top-up. If the balance falls below this amount, a top-up is initiated."""


class Trigger1Dict(TypedDict):
    schedule: NotRequired[Schedule21 | Schedule21Dict]
    threshold: Amount17 | Amount17Dict
