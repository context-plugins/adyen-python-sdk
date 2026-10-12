from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .print_output2 import PrintOutput2, PrintOutput2Dict


class PrintRequest2(SdkBaseModel):
    """Content of the Print Request message."""

    print_output: PrintOutput2 = Field(alias="PrintOutput")
    """Information to print and how to process it."""


class PrintRequest2Dict(TypedDict):
    print_output: PrintOutput2Dict
