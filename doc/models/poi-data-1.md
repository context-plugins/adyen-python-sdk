
# Poi Data 1

Data related to the POI System.

*This model accepts additional fields of type Any.*

## Structure

`PoiData1`

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

from adyen.models.poi_data_1 import PoiData1
from adyen.models.poi_transaction_id import PoiTransactionId

poi_data_1 = PoiData1(
    poi_transaction_id=PoiTransactionId(
        transaction_id='TransactionID2',
        time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    poi_reconciliation_id=252,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

