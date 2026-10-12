from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .display_output2 import DisplayOutput2, DisplayOutput2Dict
from .input_data2 import InputData2, InputData2Dict


class InputRequest(SdkBaseModel):
    """Content of the ``InputRequest`` message. It conveys the data to display and how to process it. In addition to the
    display on the Input Device, it might contain an operation (the ``DisplayOutput`` element) per Display Device
    type."""

    display_output: Optional[DisplayOutput2] = Field(default=UNSET, alias="DisplayOutput")
    """Information to display and the way to process the display."""

    input_data: InputData2 = Field(alias="InputData")
    """Information related to an Input request. It conveys the target input logical device, the type of input command,
    and possible minimum and maximum length of the input. In addition, if the requestor might require to receive an
    Event Notification if a card is inserted in a card reader, with the ``NotifyCardInputFlag``."""


class InputRequestDict(TypedDict):
    display_output: NotRequired[DisplayOutput2Dict]
    input_data: InputData2Dict
