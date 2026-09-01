from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .display_output import DisplayOutput, DisplayOutputDict


class DisplayRequest(SdkBaseModel):
    """It conveys the data to display and the way to process the display. It contains the complete content to display.
    It might contain an operation (the DisplayOutput element) per Display Device type. Content of the Display Request
    message."""

    display_output: list[DisplayOutput] = Field(alias="DisplayOutput")
    """Information to display and the way to process the display. Complete display content for output devices. At most
    one DisplayOutput per Device/ InfoQualify pair."""


class DisplayRequestDict(TypedDict):
    display_output: list[DisplayOutput | DisplayOutputDict]
