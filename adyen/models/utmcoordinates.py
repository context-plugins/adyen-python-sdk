from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Utmcoordinates(SdkBaseModel):
    utm_zone: str = Field(alias="UTMZone")
    """UTM grid zone combination of the longitude zone (1 to 60) and the latitude band (C to X, excluding I and O)."""

    utm_eastward: str = Field(alias="UTMEastward")
    """X-coordinate of the Universal Transverse Mercator coordinate system."""

    utm_northward: str = Field(alias="UTMNorthward")
    """Y-coordinate of the Universal Transverse Mercator coordinate system."""


class UtmcoordinatesDict(TypedDict):
    utm_zone: str
    utm_eastward: str
    utm_northward: str
