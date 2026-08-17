
# Sale Terminal Data 2

Information related to the software and hardware feature of the Sale Terminal.
Present if the login involve a Sale Terminal.

## Structure

`SaleTerminalData2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `totals_group_id` | `str` | Optional | Identification of a group of transactions on a POI Terminal, having the same Sale features.<br>Could be used to group POI for reconciliation or other purpose defined by the Sale System. The default value is assigned by the Login Request.<br><br>**Constraints**: *Pattern*: `^.{1,16}$` |

## Example

```python
from adyen.models.sale_terminal_data_2 import SaleTerminalData2

sale_terminal_data_2 = SaleTerminalData2(
    totals_group_id='TotalsGroupID6'
)
```

