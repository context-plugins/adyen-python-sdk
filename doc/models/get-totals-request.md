
# Get Totals Request

It conveys information from the Sale System related to the scope and the format of the totals to be computed by the POI System.
Content of the Get Totals Request message.

*This model accepts additional fields of type Any.*

## Structure

`GetTotalsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_details` | [`List[TotalDetail]`](../../doc/models/total-detail.md) | Optional | Indicates the hierarchical structure of the reconciliation result of the Sale to POI reconciliation.<br>Required to present totals per value of element included in this cluster (POI Terminal, Sale Terminal, Cashier, Shift, TotalsGroupID).<br>Possible values:<br><br>* **OperatorID**<br>* **POIID**<br>* **SaleID**<br>* **ShiftNumber**<br>* **TotalsGroupID** |
| `total_filter` | [`TotalFilter`](../../doc/models/total-filter.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.get_totals_request import GetTotalsRequest
from adyen.models.total_detail import TotalDetail
from adyen.models.total_filter import TotalFilter

get_totals_request = GetTotalsRequest(
    total_details=[
        TotalDetail.TOTALSGROUPID
    ],
    total_filter=TotalFilter(
        poiid='POIID6',
        sale_id='SaleID8',
        operator_id='OperatorID8',
        shift_number='ShiftNumber0',
        totals_group_id='TotalsGroupID0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

