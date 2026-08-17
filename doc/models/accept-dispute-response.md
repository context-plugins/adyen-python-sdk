
# Accept Dispute Response

## Structure

`AcceptDisputeResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_service_result` | [`DisputeServiceResult1`](../../doc/models/dispute-service-result-1.md) | Required | The result of the dispute service. |

## Example

```python
from adyen.models.accept_dispute_response import AcceptDisputeResponse
from adyen.models.dispute_service_result_1 import DisputeServiceResult1

accept_dispute_response = AcceptDisputeResponse(
    dispute_service_result=DisputeServiceResult1(
        success=False,
        error_message='errorMessage8'
    )
)
```

