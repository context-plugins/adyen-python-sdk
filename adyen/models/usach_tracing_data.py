from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class UsachTracingData(SdkBaseModel):
    trace_number: str = Field(alias="traceNumber")
    """The ACH trace number. This is a unique 15-digit identifier assigned to transfers processed by `ACH
    <https://fiscal.treasury.gov/payments-from-government/automated-clearing-house-ach>`__."""

    type_: Literal["usAch"] = Field(default="usAch", alias="type")
    """**usAch**"""


class UsachTracingDataDict(TypedDict):
    trace_number: str
    type_: NotRequired[Literal["usAch"]]
