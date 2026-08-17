
# POI Data 4

Data related to the POI System.
If Result is Success.

## Structure

`POIData4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `poi_transaction_id` | [`TransactionIDType2`](../../doc/models/transaction-id-type-2.md) | Required | Unique identification of a POI transaction for a POI. |
| `poi_reconciliation_id` | `int` | Optional | Identification of the reconciliation period between Sale and POI.<br>If Result is Success. |

## Example

```python
import dateutil.parser

from adyen.models.poi_data_4 import POIData4
from adyen.models.transaction_id_type_2 import TransactionIDType2

poi_data_4 = POIData4(
    poi_transaction_id=TransactionIDType2(
        transaction_id='TransactionID2',
        time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    ),
    poi_reconciliation_id=104
)
```

