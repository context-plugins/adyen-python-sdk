from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class EstimationTrackingData(SdkBaseModel):
    estimated_arrival_time: RFC3339DateTime = Field(alias="estimatedArrivalTime")
    """The estimated time the beneficiary should have access to the funds."""

    type_: Literal["estimation"] = Field(default="estimation", alias="type")
    """The type of tracking event.

    Possible values:

    - **estimation**: the estimated date and time of when the funds will be credited has been determined."""


class EstimationTrackingDataDict(TypedDict):
    estimated_arrival_time: RFC3339DateTime
    type_: NotRequired[Literal["estimation"]]
