
# Issuing Transaction Data

*This model accepts additional fields of type Any.*

## Structure

`IssuingTransactionData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `capture_cycle_id` | `str` | Optional | captureCycleId associated with transfer event. |
| `mtype` | [`Type86`](../../doc/models/type-86.md) | Required | The type of events data.<br><br>Possible values:<br><br>- **issuingTransactionData**: issuing transaction data |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.issuing_transaction_data import IssuingTransactionData
from adyen.models.type_86 import Type86

issuing_transaction_data = IssuingTransactionData(
    mtype=Type86.ISSUINGTRANSACTIONDATA,
    capture_cycle_id='captureCycleId6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

