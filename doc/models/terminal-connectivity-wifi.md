
# Terminal Connectivity Wifi

## Structure

`TerminalConnectivityWifi`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ip_address` | `str` | Optional | The terminal's IP address in the Wi-Fi network. |
| `mac_address` | `str` | Optional | The terminal's MAC address in the Wi-Fi network. |
| `ssid` | `str` | Optional | The SSID of the Wi-Fi network that the terminal is connected to. |

## Example

```python
from adyen.models.terminal_connectivity_wifi import TerminalConnectivityWifi

terminal_connectivity_wifi = TerminalConnectivityWifi(
    ip_address='ipAddress0',
    mac_address='macAddress4',
    ssid='ssid2'
)
```

