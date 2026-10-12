from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..ukfps_tracing_data import UkfpsTracingData, UkfpsTracingDataDict
from ..usach_tracing_data import UsachTracingData, UsachTracingDataDict

Tracing: TypeAlias = Annotated[
    Annotated[UkfpsTracingData, Tag("ukFps")] | Annotated[UsachTracingData, Tag("usAch")], WireDiscriminator("type")
]
"""Contains information for tracing the transfer after Adyen forwards it to the network."""

TracingDict: TypeAlias = UkfpsTracingDataDict | UsachTracingDataDict
