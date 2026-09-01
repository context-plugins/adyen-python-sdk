from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class KioskModeSettings(SdkBaseModel):
    allowed_apps_in_kiosk_mode: Optional[list[str]] = Field(default=UNSET, alias="allowedAppsInKioskMode")
    """List of package names for apps allowed to run in kiosk mode."""

    kiosk_app_on_startup: Optional[str] = Field(default=UNSET, alias="kioskAppOnStartup")
    """The package name of the app to launch on startup. This must be one of the apps included in
    ``allowedAppsInKioskMode``."""


class KioskModeSettingsDict(TypedDict):
    allowed_apps_in_kiosk_mode: NotRequired[list[str]]
    kiosk_app_on_startup: NotRequired[str]
