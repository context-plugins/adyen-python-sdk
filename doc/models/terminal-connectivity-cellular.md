
# Terminal Connectivity Cellular

## Structure

`TerminalConnectivityCellular`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `iccid` | `str` | Optional | The integrated circuit card identifier (ICCID) of the primary SIM card in the terminal. |
| `iccid_2` | `str` | Optional | The integrated circuit card identifier (ICCID) of the secondary SIM card in the terminal, typically used for a [third-party SIM card](https://docs.adyen.com/point-of-sale/design-your-integration/network-and-connectivity/cellular-failover/#using-a-third-party-sim-card). |
| `status` | [`Status31Enum`](../../doc/models/status-31-enum.md) | Optional | On a terminal that supports 3G or 4G connectivity, indicates the status of the primary SIM card in the terminal. |

## Example

```python
from adyen.models.status_31_enum import Status31Enum
from adyen.models.terminal_connectivity_cellular import TerminalConnectivityCellular

terminal_connectivity_cellular = TerminalConnectivityCellular(
    iccid='iccid0',
    iccid_2='iccid22',
    status=Status31Enum.READYFORACTIVATION
)
```

