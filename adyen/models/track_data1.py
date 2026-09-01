from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.track_format1 import TrackFormat1OrStr


class TrackData1(SdkBaseModel):
    """Magnetic track or magnetic ink characters line. Mandatory if CheckNumber absent."""

    track_numb: Optional[int] = Field(default=UNSET, alias="TrackNumb")
    """Card track number."""

    track_format: Optional[TrackFormat1OrStr] = Field(default=UNSET, alias="TrackFormat")
    """Card track format. Possible values:
    * **AAMVA**
    * **ISO**"""

    track_value: str = Field(alias="TrackValue")
    """Card track content."""


class TrackData1Dict(TypedDict):
    track_numb: NotRequired[int]
    track_format: NotRequired[TrackFormat1OrStr]
    track_value: str
