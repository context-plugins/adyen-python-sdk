from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ScreenDimensions(SdkBaseModel):
    height: Optional[int] = UNSET
    width: Optional[int] = UNSET


class ScreenDimensionsDict(TypedDict):
    height: NotRequired[int]
    width: NotRequired[int]
