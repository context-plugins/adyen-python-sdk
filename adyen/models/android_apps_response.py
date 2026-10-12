from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .android_app import AndroidApp, AndroidAppDict


class AndroidAppsResponse(SdkBaseModel):
    data: Optional[list[AndroidApp]] = UNSET
    """Apps uploaded for Android payment terminals."""


class AndroidAppsResponseDict(TypedDict):
    data: NotRequired[list[AndroidAppDict]]
