from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Hardware(SdkBaseModel):
    display_maximum_back_light: Optional[int] = Field(default=UNSET, alias="displayMaximumBackLight")
    """The brightness of the display when the terminal is being used, expressed as a percentage."""

    reset_totals_hour: Optional[int] = Field(default=UNSET, alias="resetTotalsHour")
    """The hour of the day when the terminal is set to reset the Totals report. By default, the reset hour is at 6:00 AM
    in the timezone of the terminal. Minimum value: 0, maximum value: 23."""

    restart_hour: Optional[int] = Field(default=UNSET, alias="restartHour")
    """The hour of the day when the terminal is set to reboot to apply the configuration and software updates. By
    default, the restart hour is at 6:00 AM in the timezone of the terminal. Minimum value: 0, maximum value: 23."""


class HardwareDict(TypedDict):
    display_maximum_back_light: NotRequired[int]
    reset_totals_hour: NotRequired[int]
    restart_hour: NotRequired[int]
