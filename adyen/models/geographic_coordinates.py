from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GeographicCoordinates(SdkBaseModel):
    latitude: str = Field(alias="Latitude")
    """Angular distance of a location on the earth south or north of the equator."""

    longitude: str = Field(alias="Longitude")
    """Angular measurement of the distance of a location on the earth east or west of the Greenwich observatory."""


class GeographicCoordinatesDict(TypedDict):
    latitude: str
    longitude: str
