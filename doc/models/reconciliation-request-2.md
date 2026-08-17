
# Reconciliation Request 2

Content of the Reconciliation Request message.

## Structure

`ReconciliationRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reconciliation_type` | [`ReconciliationType1Enum`](../../doc/models/reconciliation-type-1-enum.md) | Required | Type of Reconciliation requested by the Sale to the POI.<br>Possible values:<br><br>* **AcquirerReconciliation**<br>* **AcquirerSynchronisation**<br>* **PreviousReconciliation**<br>* **SaleReconciliation** |
| `acquirer_id` | `List[int]` | Optional | Identification of the Acquirer.<br>Could be present only if ReconciliationType is AcquirerReconciliation or AcquirerSynchronisation. |
| `poi_reconciliation_id` | `int` | Optional | Identification of the reconciliation period between Sale and POI.<br>Absent if ReconciliationType is not PreviousReconciliation. |

## Example

```python
from adyen.models.reconciliation_request_2 import ReconciliationRequest2
from adyen.models.reconciliation_type_1_enum import ReconciliationType1Enum

reconciliation_request_2 = ReconciliationRequest2(
    reconciliation_type=ReconciliationType1Enum.ACQUIRERRECONCILIATION,
    acquirer_id=[
        62,
        61,
        60
    ],
    poi_reconciliation_id=104
)
```

