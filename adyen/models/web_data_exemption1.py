from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.reason3 import Reason3OrStr


class WebDataExemption1(SdkBaseModel):
    """The reason why the web data is not provided."""

    reason: Optional[Reason3OrStr] = UNSET
    """The reason why the web data was not provided. Possible value: **noOnlinePresence**."""


class WebDataExemption1Dict(TypedDict):
    reason: NotRequired[Reason3OrStr]
