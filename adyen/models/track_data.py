from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.track_format1 import TrackFormat1OrStr


class TrackData(SdkBaseModel):
    """Magnetic track or magnetic ink characters line. ISO 7813 - ISO 4909. Generic data structure for a card track,
    used when the magstripe card reader is located on the Sale Terminal, or for magstripe Card Reader device request.
    The data structure is also used to store the line at the bottom of a bank check."""

    track_numb: int = Field(default=2, alias="TrackNumb")
    """Card track number."""

    track_format: Optional[TrackFormat1OrStr] = Field(default=UNSET, alias="TrackFormat")
    """Card track format. Possible values:
    * **AAMVA**
    * **ISO**"""

    track_value: str = Field(alias="TrackValue")
    """Card track content."""


class TrackDataDict(TypedDict):
    track_numb: NotRequired[int]
    track_format: NotRequired[TrackFormat1OrStr]
    track_value: str
