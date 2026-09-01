from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .poisoftware import Poisoftware, PoisoftwareDict
from .poistatus import Poistatus, PoistatusDict


class PoisystemData1(SdkBaseModel):
    """Information related to the POI System. Returned if the response result is Success."""

    date_time: RFC3339DateTime = Field(alias="DateTime")
    """Date and Time. In the response, the POI System gives its date and time to the Sale System."""

    poi_software: Poisoftware = Field(alias="POISoftware")
    """Information related to the software of the POI System which manages the Sale to POI protocol. In a session allows
    identifying the product features of a POI System."""

    poi_status: Optional[Poistatus] = Field(default=UNSET, alias="POIStatus")
    """Indicate the availability of the POI Terminal components. The data element is absent if the component is not part
    of the POI Terminal. State of a POI Terminal."""


class PoisystemData1Dict(TypedDict):
    date_time: RFC3339DateTime
    poi_software: Poisoftware | PoisoftwareDict
    poi_status: NotRequired[Poistatus | PoistatusDict]
