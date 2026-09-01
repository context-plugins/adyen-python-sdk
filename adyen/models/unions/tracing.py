from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Field

from ..ukfps_tracing_data import UkfpsTracingData, UkfpsTracingDataDict
from ..usach_tracing_data import UsachTracingData, UsachTracingDataDict

Tracing: TypeAlias = Annotated[UkfpsTracingData | UsachTracingData, Field(discriminator="type_")]
"""Contains information for tracing the transfer after Adyen forwards it to the network."""

TracingDict: TypeAlias = UkfpsTracingDataDict | UsachTracingDataDict
