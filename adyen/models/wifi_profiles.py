from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .profile import Profile, ProfileDict
from .settings1 import Settings1, Settings1Dict


class WifiProfiles(SdkBaseModel):
    profiles: Optional[list[Profile]] = UNSET
    """List of remote Wi-Fi profiles."""

    settings: Optional[Settings1] = UNSET
    """General Wi-Fi settings."""


class WifiProfilesDict(TypedDict):
    profiles: NotRequired[list[ProfileDict]]
    settings: NotRequired[Settings1Dict]
