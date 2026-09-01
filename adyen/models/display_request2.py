from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .display_output import DisplayOutput, DisplayOutputDict


class DisplayRequest2(SdkBaseModel):
    """Content of the Display Request message."""

    display_output: list[DisplayOutput] = Field(alias="DisplayOutput")
    """Information to display and the way to process the display. Complete display content for output devices. At most
    one DisplayOutput per Device/ InfoQualify pair."""


class DisplayRequest2Dict(TypedDict):
    display_output: list[DisplayOutput | DisplayOutputDict]
