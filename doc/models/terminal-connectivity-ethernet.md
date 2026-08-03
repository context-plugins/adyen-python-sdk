
# Terminal Connectivity Ethernet

*This model accepts additional fields of type Any.*

## Structure

`TerminalConnectivityEthernet`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ip_address` | `str` | Optional | The terminal's ethernet IP address. |
| `link_negotiation` | `str` | Optional | The ethernet link negotiation that the terminal uses. |
| `mac_address` | `str` | Optional | The terminal's ethernet MAC address. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.terminal_connectivity_ethernet import TerminalConnectivityEthernet

terminal_connectivity_ethernet = TerminalConnectivityEthernet(
    ip_address='ipAddress2',
    link_negotiation='linkNegotiation6',
    mac_address='macAddress2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

