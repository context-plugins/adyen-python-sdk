
# Terminal Connectivity Bluetooth

## Structure

`TerminalConnectivityBluetooth`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ip_address` | `str` | Optional | The terminal's Bluetooth IP address. |
| `mac_address` | `str` | Optional | The terminal's Bluetooth MAC address. |

## Example

```python
from adyen.models.terminal_connectivity_bluetooth import TerminalConnectivityBluetooth

terminal_connectivity_bluetooth = TerminalConnectivityBluetooth(
    ip_address='ipAddress8',
    mac_address='macAddress6'
)
```

