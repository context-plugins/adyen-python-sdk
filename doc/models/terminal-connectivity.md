
# Terminal Connectivity

## Structure

`TerminalConnectivity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bluetooth` | [`TerminalConnectivityBluetooth`](../../doc/models/terminal-connectivity-bluetooth.md) | Optional | - |
| `cellular` | [`TerminalConnectivityCellular`](../../doc/models/terminal-connectivity-cellular.md) | Optional | - |
| `ethernet` | [`TerminalConnectivityEthernet`](../../doc/models/terminal-connectivity-ethernet.md) | Optional | - |
| `wifi` | [`TerminalConnectivityWifi`](../../doc/models/terminal-connectivity-wifi.md) | Optional | - |

## Example

```python
from adyen.models.status_31_enum import Status31Enum
from adyen.models.terminal_connectivity import TerminalConnectivity
from adyen.models.terminal_connectivity_bluetooth import TerminalConnectivityBluetooth
from adyen.models.terminal_connectivity_cellular import TerminalConnectivityCellular
from adyen.models.terminal_connectivity_ethernet import TerminalConnectivityEthernet
from adyen.models.terminal_connectivity_wifi import TerminalConnectivityWifi

terminal_connectivity = TerminalConnectivity(
    bluetooth=TerminalConnectivityBluetooth(
        ip_address='ipAddress2',
        mac_address='macAddress2'
    ),
    cellular=TerminalConnectivityCellular(
        iccid='iccid6',
        iccid_2='iccid24',
        status=Status31Enum.DEPRECATED
    ),
    ethernet=TerminalConnectivityEthernet(
        ip_address='ipAddress2',
        link_negotiation='linkNegotiation6',
        mac_address='macAddress2'
    ),
    wifi=TerminalConnectivityWifi(
        ip_address='ipAddress8',
        mac_address='macAddress6',
        ssid='ssid4'
    )
)
```

