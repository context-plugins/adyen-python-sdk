from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .input_result2 import InputResult2, InputResult2Dict
from .output_result1 import OutputResult1, OutputResult1Dict


class InputResponse2(SdkBaseModel):
    """Content of the Input Response message."""

    output_result: Optional[OutputResult1] = Field(default=UNSET, alias="OutputResult")
    """Information related to the result the output (display, print, input). If DisplayOutput present in the request."""

    input_result: InputResult2 = Field(alias="InputResult")
    """Contains the result and the content of the input."""


class InputResponse2Dict(TypedDict):
    output_result: NotRequired[OutputResult1Dict]
    input_result: InputResult2Dict
