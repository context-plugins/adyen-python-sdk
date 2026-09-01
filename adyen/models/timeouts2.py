from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Timeouts2(SdkBaseModel):
    """Settings for device `time-outs <https://docs.adyen.com/point-of-sale/pos-timeouts#device-time-out>`__."""

    from_active_to_sleep: Optional[int] = Field(default=UNSET, alias="fromActiveToSleep")
    """Indicates the number of seconds of inactivity after which the terminal display goes into sleep mode."""


class Timeouts2Dict(TypedDict):
    from_active_to_sleep: NotRequired[int]
