from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Timeouts(SdkBaseModel):
    from_active_to_sleep: Optional[int] = Field(default=UNSET, alias="fromActiveToSleep")
    """Indicates the number of seconds of inactivity after which the terminal display goes into sleep mode."""


class TimeoutsDict(TypedDict):
    from_active_to_sleep: NotRequired[int]
