from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .sweep_configuration_v2 import SweepConfigurationV2, SweepConfigurationV2Dict


class BalanceSweepConfigurationsResponse(SdkBaseModel):
    has_next: bool = Field(alias="hasNext")
    """Indicates whether there are more items on the next page."""

    has_previous: bool = Field(alias="hasPrevious")
    """Indicates whether there are more items on the previous page."""

    sweeps: list[SweepConfigurationV2]
    """List of sweeps associated with the balance account."""


class BalanceSweepConfigurationsResponseDict(TypedDict):
    has_next: bool
    has_previous: bool
    sweeps: list[SweepConfigurationV2Dict]
