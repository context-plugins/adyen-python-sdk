
# Total Filter 2

Filter to compute the totals.
Used for the Get Totals, to request totals for a (or a combination of) particular value of the POI Terminal, Sale Terminal, Cashier, Shift, or TotalsGroupID.

## Structure

`TotalFilter2`

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
from adyen.models.total_filter_2 import TotalFilter2

total_filter_2 = TotalFilter2(
    poiid='POIID2',
    sale_id='SaleID2',
    operator_id='OperatorID2',
    shift_number='ShiftNumber4',
    totals_group_id='TotalsGroupID6'
)
```

