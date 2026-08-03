
# Accept Dispute Response

*This model accepts additional fields of type Any.*

## Structure

`AcceptDisputeResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_service_result` | [`DisputeServiceResult`](../../doc/models/dispute-service-result.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.accept_dispute_response import AcceptDisputeResponse
from adyen.models.dispute_service_result import DisputeServiceResult

accept_dispute_response = AcceptDisputeResponse(
    dispute_service_result=DisputeServiceResult(
        success=False,
        error_message='errorMessage8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

