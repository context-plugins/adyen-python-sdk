
# Sale Terminal Data 1

Information related to the software and hardware features of the Sale Terminal.
If content is not empty.

## Structure

`SaleTerminalData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `totals_group_id` | `str` | Optional | Identification of a group of transactions on a POI Terminal, having the same Sale features.<br>Could be used to group POI for reconciliation or other purpose defined by the Sale System. The default value is assigned by the Login Request.<br><br>**Constraints**: *Pattern*: `^.{1,16}$` |

## Example

```python
from adyen.models.sale_terminal_data_1 import SaleTerminalData1

sale_terminal_data_1 = SaleTerminalData1(
    totals_group_id='TotalsGroupID4'
)
```

