from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .output_result import OutputResult, OutputResultDict


class DisplayResponse(SdkBaseModel):
    """It conveys the result of the display, parallel to the message request, except if response not required and
    absent. Content of the Display Response message."""

    output_result: list[OutputResult] = Field(alias="OutputResult")
    """Information related to the result the output (display, print, input). One per DisplayOutput item of the request,
    and in the same order."""


class DisplayResponseDict(TypedDict):
    output_result: list[OutputResultDict]
