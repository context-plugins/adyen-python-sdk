from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .profile import Profile, ProfileDict
from .settings1 import Settings1, Settings1Dict


class WifiProfiles2(SdkBaseModel):
    """Remote Wi-Fi profiles for WPA and WPA2 PSK and EAP Wi-Fi networks."""

    profiles: Optional[list[Profile]] = UNSET
    """List of remote Wi-Fi profiles."""

    settings: Optional[Settings1] = UNSET
    """General Wi-Fi settings."""


class WifiProfiles2Dict(TypedDict):
    profiles: NotRequired[list[Profile | ProfileDict]]
    settings: NotRequired[Settings1 | Settings1Dict]
