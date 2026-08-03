
# Terminal Connectivity 2

Information about bluetooth, cellular, ethernet and wifi connectivity for the terminal.

*This model accepts additional fields of type Any.*

## Structure

`TerminalConnectivity2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bluetooth` | [`TerminalConnectivityBluetooth`](../../doc/models/terminal-connectivity-bluetooth.md) | Optional | - |
| `cellular` | [`TerminalConnectivityCellular`](../../doc/models/terminal-connectivity-cellular.md) | Optional | - |
| `ethernet` | [`TerminalConnectivityEthernet`](../../doc/models/terminal-connectivity-ethernet.md) | Optional | - |
| `wifi` | [`TerminalConnectivityWifi`](../../doc/models/terminal-connectivity-wifi.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.status_32 import Status32
from adyen.models.terminal_connectivity_2 import TerminalConnectivity2
from adyen.models.terminal_connectivity_bluetooth import TerminalConnectivityBluetooth
from adyen.models.terminal_connectivity_cellular import TerminalConnectivityCellular
from adyen.models.terminal_connectivity_ethernet import TerminalConnectivityEthernet
from adyen.models.terminal_connectivity_wifi import TerminalConnectivityWifi

terminal_connectivity_2 = TerminalConnectivity2(
    bluetooth=TerminalConnectivityBluetooth(
        ip_address='ipAddress2',
        mac_address='macAddress2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    cellular=TerminalConnectivityCellular(
        iccid='iccid6',
        iccid_2='iccid24',
        status=Status32.DEPRECATED,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    ethernet=TerminalConnectivityEthernet(
        ip_address='ipAddress2',
        link_negotiation='linkNegotiation6',
        mac_address='macAddress2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    wifi=TerminalConnectivityWifi(
        ip_address='ipAddress8',
        mac_address='macAddress6',
        ssid='ssid4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

