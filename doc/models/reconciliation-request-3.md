
# Reconciliation Request 3

*This model accepts additional fields of type Any.*

## Structure

`ReconciliationRequest3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reconciliation_type` | [`ReconciliationType1`](../../doc/models/reconciliation-type-1.md) | Required | - |
| `acquirer_id` | `List[int]` | Optional | Identification of the Acquirer.<br>Could be present only if ReconciliationType is AcquirerReconciliation or AcquirerSynchronisation. |
| `poi_reconciliation_id` | `int` | Optional | Identification of the reconciliation period between Sale and POI.<br>Absent if ReconciliationType is not PreviousReconciliation. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.reconciliation_request_3 import ReconciliationRequest3
from adyen.models.reconciliation_type_1 import ReconciliationType1

reconciliation_request_3 = ReconciliationRequest3(
    reconciliation_type=ReconciliationType1.ACQUIRERRECONCILIATION,
    acquirer_id=[
        154,
        153,
        152
    ],
    poi_reconciliation_id=128,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

