from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .print_output2 import PrintOutput2, PrintOutput2Dict


class PrintRequest(SdkBaseModel):
    """Content of the Print Request message. It conveys the complete data to print and how to process the print."""

    print_output: PrintOutput2 = Field(alias="PrintOutput")
    """Information to print and how to process it."""


class PrintRequestDict(TypedDict):
    print_output: PrintOutput2Dict
