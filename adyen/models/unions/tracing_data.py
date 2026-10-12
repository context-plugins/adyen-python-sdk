from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..ukfps_tracing_data import UkfpsTracingData, UkfpsTracingDataDict
from ..usach_tracing_data import UsachTracingData, UsachTracingDataDict

TracingData: TypeAlias = Annotated[
    Annotated[UkfpsTracingData, Tag("ukFps")] | Annotated[UsachTracingData, Tag("usAch")], WireDiscriminator("type")
]
"""Additional tracing information for the tracing event."""

TracingDataDict: TypeAlias = UkfpsTracingDataDict | UsachTracingDataDict
