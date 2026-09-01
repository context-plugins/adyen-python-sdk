from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Settings(SdkBaseModel):
    band: Optional[str] = UNSET
    """The preferred Wi-Fi band, for use if the terminals support multiple bands. Possible values: All, 2.4GHz, 5GHz."""

    roaming: Optional[bool] = UNSET
    """Indicates whether roaming is enabled on the terminals."""

    timeout: Optional[int] = UNSET
    """The connection time-out in seconds. Minimum value: 0."""


class SettingsDict(TypedDict):
    band: NotRequired[str]
    roaming: NotRequired[bool]
    timeout: NotRequired[int]
