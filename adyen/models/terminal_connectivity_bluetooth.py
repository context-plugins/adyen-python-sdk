from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TerminalConnectivityBluetooth(SdkBaseModel):
    ip_address: Optional[str] = Field(default=UNSET, alias="ipAddress")
    """The terminal's Bluetooth IP address."""

    mac_address: Optional[str] = Field(default=UNSET, alias="macAddress")
    """The terminal's Bluetooth MAC address."""


class TerminalConnectivityBluetoothDict(TypedDict):
    ip_address: NotRequired[str]
    mac_address: NotRequired[str]
