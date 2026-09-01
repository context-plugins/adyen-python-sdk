from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .host_status import HostStatus, HostStatusDict
from .poistatus1 import Poistatus1, Poistatus1Dict
from .response11 import Response11, Response11Dict


class DiagnosisResponse2(SdkBaseModel):
    """Content of the Diagnosis Response message."""

    response: Response11 = Field(alias="Response")
    """Result of a message request processing."""

    poi_status: Optional[Poistatus1] = Field(default=UNSET, alias="POIStatus")
    """State of a POI Terminal. If ``Response.Result`` is Success."""

    host_status: Optional[list[HostStatus]] = Field(default=UNSET, alias="HostStatus")
    """State of a Host."""


class DiagnosisResponse2Dict(TypedDict):
    response: Response11 | Response11Dict
    poi_status: NotRequired[Poistatus1 | Poistatus1Dict]
    host_status: NotRequired[list[HostStatus | HostStatusDict]]
