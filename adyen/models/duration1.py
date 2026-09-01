from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.unit import UnitOrStr


class Duration1(SdkBaseModel):
    """The duration, which you can specify in hours, days, weeks, or months. The maximum duration is 90 days or an
    equivalent in other units. Required when the ``type`` is **rolling** or **sliding**."""

    unit: Optional[UnitOrStr] = UNSET
    """The unit of time. You can only use **minutes** and **hours** if the ``interval.type`` is **sliding**.

    Possible values: **minutes**, **hours**, **days**, **weeks**, or **months**"""

    value: Optional[int] = UNSET
    """The length of time by the unit. For example, 5 days.

    The maximum duration is 90 days or an equivalent in other units. For example, 3 months."""


class Duration1Dict(TypedDict):
    unit: NotRequired[UnitOrStr]
    value: NotRequired[int]
