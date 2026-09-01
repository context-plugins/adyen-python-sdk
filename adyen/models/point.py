from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Point(SdkBaseModel):
    x: str = Field(alias="X")
    """The hexadecimal value of the coordinates of a point on the abscissa."""

    y: str = Field(alias="Y")
    """The hexadecimal value of the coordinates of a point on the ordinate."""


class PointDict(TypedDict):
    x: str
    y: str
