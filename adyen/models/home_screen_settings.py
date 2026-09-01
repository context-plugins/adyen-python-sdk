from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class HomeScreenSettings(SdkBaseModel):
    hide_navigation_bar: Optional[bool] = Field(default=UNSET, alias="hideNavigationBar")
    """Hide/show the navigation bar."""

    show_payments_menu: Optional[bool] = Field(default=UNSET, alias="showPaymentsMenu")
    """Show/hide the payments menu."""

    show_settings_menu: Optional[bool] = Field(default=UNSET, alias="showSettingsMenu")
    """Show/hide the settings menu."""


class HomeScreenSettingsDict(TypedDict):
    hide_navigation_bar: NotRequired[bool]
    show_payments_menu: NotRequired[bool]
    show_settings_menu: NotRequired[bool]
