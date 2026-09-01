from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AreaSize1(SdkBaseModel):
    """Size of an area. Contain the size of the pad area where the signature is written, given with the maximum abscissa
    and ordinate values (X and Y). The maximum value is FFFF."""

    x: str = Field(alias="X")
    """Abscissa of a point coordinates. The hexadecimal value in text of the abscissa of the coordinates of a point.
    Leading zero can be removed (e.g. 3BC, 0, and 1287)."""

    y: str = Field(alias="Y")
    """Ordinate of a point coordinates. The hexadecimal value in text of the ordinate of the coordinates of a point.
    Leading zero can be removed (e.g. 3BC, 0, and 1287)."""


class AreaSize1Dict(TypedDict):
    x: str
    y: str
