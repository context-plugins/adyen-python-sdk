from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .area_size1 import AreaSize1, AreaSize1Dict
from .point import Point, PointDict


class CapturedSignature(SdkBaseModel):
    area_size: Optional[AreaSize1] = Field(default=UNSET, alias="AreaSize")
    """Size of an area. Contain the size of the pad area where the signature is written, given with the maximum abscissa
    and ordinate values (X and Y). The maximum value is FFFF."""

    signature_point: Optional[list[Point]] = Field(default=UNSET, alias="SignaturePoint")
    """Coordinates of a point where the pen changes direction or lift. Contain the Coordinates of a point of the written
    signature where the pen changes direction or lift where (X and Y). When the signer lifts the pen, both X and Y have
    the value FFFF."""


class CapturedSignatureDict(TypedDict):
    area_size: NotRequired[AreaSize1Dict]
    signature_point: NotRequired[list[PointDict]]
