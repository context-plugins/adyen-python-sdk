
# Terminal Connectivity Ethernet

## Structure

`TerminalConnectivityEthernet`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ip_address` | `str` | Optional | The terminal's ethernet IP address. |
| `link_negotiation` | `str` | Optional | The ethernet link negotiation that the terminal uses. |
| `mac_address` | `str` | Optional | The terminal's ethernet MAC address. |

## Example

```python
from adyen.models.terminal_connectivity_ethernet import TerminalConnectivityEthernet

terminal_connectivity_ethernet = TerminalConnectivityEthernet(
    ip_address='ipAddress2',
    link_negotiation='linkNegotiation6',
    mac_address='macAddress2'
)
```

