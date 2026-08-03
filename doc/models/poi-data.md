
# Poi Data

Data related to the POI System.
In the Message Response, identification of the POI transaction.

*This model accepts additional fields of type Any.*

## Structure

`PoiData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `poi_transaction_id` | [`PoiTransactionId`](../../doc/models/poi-transaction-id.md) | Required | - |
| `poi_reconciliation_id` | `int` | Optional | Identification of the reconciliation period between Sale and POI.<br>If Result is Success. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.poi_data import PoiData
from adyen.models.poi_transaction_id import PoiTransactionId

poi_data = PoiData(
    poi_transaction_id=PoiTransactionId(
        transaction_id='TransactionID2',
        time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    poi_reconciliation_id=94,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

