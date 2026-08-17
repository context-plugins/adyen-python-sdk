
# Defend Dispute Response

## Structure

`DefendDisputeResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_service_result` | [`DisputeServiceResult1`](../../doc/models/dispute-service-result-1.md) | Required | The result of the dispute service. |

## Example

```python
from adyen.models.defend_dispute_response import DefendDisputeResponse
from adyen.models.dispute_service_result_1 import DisputeServiceResult1

defend_dispute_response = DefendDisputeResponse(
    dispute_service_result=DisputeServiceResult1(
        success=False,
        error_message='errorMessage8'
    )
)
```

