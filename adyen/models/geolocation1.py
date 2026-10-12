from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .geographic_coordinates import GeographicCoordinates, GeographicCoordinatesDict
from .utmcoordinates import Utmcoordinates, UtmcoordinatesDict


class Geolocation1(SdkBaseModel):
    """Geographic location specified by geographic or UTM coordinates. If data available."""

    geographic_coordinates: Optional[GeographicCoordinates] = Field(default=UNSET, alias="GeographicCoordinates")
    utm_coordinates: Optional[Utmcoordinates] = Field(default=UNSET, alias="UTMCoordinates")


class Geolocation1Dict(TypedDict):
    geographic_coordinates: NotRequired[GeographicCoordinatesDict]
    utm_coordinates: NotRequired[UtmcoordinatesDict]
