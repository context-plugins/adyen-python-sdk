
# Terminal Connectivity Bluetooth

*This model accepts additional fields of type Any.*

## Structure

`TerminalConnectivityBluetooth`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ip_address` | `str` | Optional | The terminal's Bluetooth IP address. |
| `mac_address` | `str` | Optional | The terminal's Bluetooth MAC address. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.terminal_connectivity_bluetooth import TerminalConnectivityBluetooth

terminal_connectivity_bluetooth = TerminalConnectivityBluetooth(
    ip_address='ipAddress8',
    mac_address='macAddress6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

