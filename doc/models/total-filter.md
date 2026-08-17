
# Total Filter

## Structure

`TotalFilter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `poiid` | `str` | Optional | Identification of a POI System or a POI Terminal for the Sale to POI protocol.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `sale_id` | `str` | Optional | Identification of a Sale System or a Sale Terminal for the Sale to POI protocol.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `operator_id` | `str` | Optional | Identification of the Cashier or Operator.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `shift_number` | `str` | Optional | Shift number.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `totals_group_id` | `str` | Optional | Sent if totals in the response have to be computed only for this particular value of TotalsGroupID.<br><br>**Constraints**: *Pattern*: `^.{1,16}$` |

## Example

```python
from adyen.models.total_filter import TotalFilter

total_filter = TotalFilter(
    poiid='POIID2',
    sale_id='SaleID6',
    operator_id='OperatorID6',
    shift_number='ShiftNumber8',
    totals_group_id='TotalsGroupID8'
)
```

