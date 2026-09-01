from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LocalTime(SdkBaseModel):
    hour: Optional[int] = UNSET
    minute: Optional[int] = UNSET
    nano: Optional[int] = UNSET
    second: Optional[int] = UNSET


class LocalTimeDict(TypedDict):
    hour: NotRequired[int]
    minute: NotRequired[int]
    nano: NotRequired[int]
    second: NotRequired[int]
