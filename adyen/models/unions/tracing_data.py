from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Field

from ..ukfps_tracing_data import UkfpsTracingData, UkfpsTracingDataDict
from ..usach_tracing_data import UsachTracingData, UsachTracingDataDict

TracingData: TypeAlias = Annotated[UkfpsTracingData | UsachTracingData, Field(discriminator="type_")]
"""Additional tracing information for the tracing event."""

TracingDataDict: TypeAlias = UkfpsTracingDataDict | UsachTracingDataDict
