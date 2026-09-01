from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.reason3 import Reason3OrStr


class WebDataExemption(SdkBaseModel):
    reason: Optional[Reason3OrStr] = UNSET
    """The reason why the web data was not provided. Possible value: **noOnlinePresence**."""


class WebDataExemptionDict(TypedDict):
    reason: NotRequired[Reason3OrStr]
