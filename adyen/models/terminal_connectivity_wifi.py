from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TerminalConnectivityWifi(SdkBaseModel):
    ip_address: Optional[str] = Field(default=UNSET, alias="ipAddress")
    """The terminal's IP address in the Wi-Fi network."""

    mac_address: Optional[str] = Field(default=UNSET, alias="macAddress")
    """The terminal's MAC address in the Wi-Fi network."""

    ssid: Optional[str] = UNSET
    """The SSID of the Wi-Fi network that the terminal is connected to."""


class TerminalConnectivityWifiDict(TypedDict):
    ip_address: NotRequired[str]
    mac_address: NotRequired[str]
    ssid: NotRequired[str]
