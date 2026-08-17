
# Sale Terminal Data

Information related to the software and hardware features of the Sale Terminal.
Sent in the Login Request if a Sale Terminal is involved in the login. In other messages, sent when a logical device is out of order (SaleCapabilities) or when other data have changed or were missing in the Login.

## Structure

`SaleTerminalData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `totals_group_id` | `str` | Optional | Identification of a group of transactions on a POI Terminal, having the same Sale features.<br>Could be used to group POI for reconciliation or other purpose defined by the Sale System. The default value is assigned by the Login Request.<br><br>**Constraints**: *Pattern*: `^.{1,16}$` |

## Example

```python
from adyen.models.sale_terminal_data import SaleTerminalData

sale_terminal_data = SaleTerminalData(
    totals_group_id='TotalsGroupID6'
)
```

