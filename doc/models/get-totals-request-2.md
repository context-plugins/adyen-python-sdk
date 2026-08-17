
# Get Totals Request 2

Content of the Get Totals Request message.

## Structure

`GetTotalsRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_details` | [`List[TotalDetailEnum]`](../../doc/models/total-detail-enum.md) | Optional | Indicates the hierarchical structure of the reconciliation result of the Sale to POI reconciliation.<br>Required to present totals per value of element included in this cluster (POI Terminal, Sale Terminal, Cashier, Shift, TotalsGroupID).<br>Possible values:<br><br>* **OperatorID**<br>* **POIID**<br>* **SaleID**<br>* **ShiftNumber**<br>* **TotalsGroupID** |
| `total_filter` | [`TotalFilter2`](../../doc/models/total-filter-2.md) | Optional | Filter to compute the totals.<br>Used for the Get Totals, to request totals for a (or a combination of) particular value of the POI Terminal, Sale Terminal, Cashier, Shift, or TotalsGroupID. |

## Example

```python
from adyen.models.get_totals_request_2 import GetTotalsRequest2
from adyen.models.total_detail_enum import TotalDetailEnum
from adyen.models.total_filter_2 import TotalFilter2

get_totals_request_2 = GetTotalsRequest2(
    total_details=[
        TotalDetailEnum.SHIFTNUMBER,
        TotalDetailEnum.TOTALSGROUPID,
        TotalDetailEnum.POIID
    ],
    total_filter=TotalFilter2(
        poiid='POIID6',
        sale_id='SaleID8',
        operator_id='OperatorID8',
        shift_number='ShiftNumber0',
        totals_group_id='TotalsGroupID0'
    )
)
```

