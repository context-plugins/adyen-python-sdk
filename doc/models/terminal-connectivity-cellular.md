
# Terminal Connectivity Cellular

*This model accepts additional fields of type Any.*

## Structure

`TerminalConnectivityCellular`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `iccid` | `str` | Optional | The integrated circuit card identifier (ICCID) of the primary SIM card in the terminal. |
| `iccid_2` | `str` | Optional | The integrated circuit card identifier (ICCID) of the secondary SIM card in the terminal, typically used for a [third-party SIM card](https://docs.adyen.com/point-of-sale/design-your-integration/network-and-connectivity/cellular-failover/#using-a-third-party-sim-card). |
| `status` | [`Status32`](../../doc/models/status-32.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.status_32 import Status32
from adyen.models.terminal_connectivity_cellular import TerminalConnectivityCellular

terminal_connectivity_cellular = TerminalConnectivityCellular(
    iccid='iccid0',
    iccid_2='iccid22',
    status=Status32.READYFORACTIVATION,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

