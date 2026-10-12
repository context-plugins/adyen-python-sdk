from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .terminal_connectivity_bluetooth import TerminalConnectivityBluetooth, TerminalConnectivityBluetoothDict
from .terminal_connectivity_cellular import TerminalConnectivityCellular, TerminalConnectivityCellularDict
from .terminal_connectivity_ethernet import TerminalConnectivityEthernet, TerminalConnectivityEthernetDict
from .terminal_connectivity_wifi import TerminalConnectivityWifi, TerminalConnectivityWifiDict


class TerminalConnectivity2(SdkBaseModel):
    """Information about bluetooth, cellular, ethernet and wifi connectivity for the terminal."""

    bluetooth: Optional[TerminalConnectivityBluetooth] = UNSET
    cellular: Optional[TerminalConnectivityCellular] = UNSET
    ethernet: Optional[TerminalConnectivityEthernet] = UNSET
    wifi: Optional[TerminalConnectivityWifi] = UNSET


class TerminalConnectivity2Dict(TypedDict):
    bluetooth: NotRequired[TerminalConnectivityBluetoothDict]
    cellular: NotRequired[TerminalConnectivityCellularDict]
    ethernet: NotRequired[TerminalConnectivityEthernetDict]
    wifi: NotRequired[TerminalConnectivityWifiDict]
