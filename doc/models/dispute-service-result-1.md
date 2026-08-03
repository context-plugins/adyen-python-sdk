
# Dispute Service Result 1

The result of the dispute service.

*This model accepts additional fields of type Any.*

## Structure

`DisputeServiceResult1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `str` | Optional | The general error message. |
| `success` | `bool` | Required | Indicates whether the request succeeded. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.dispute_service_result_1 import DisputeServiceResult1

dispute_service_result_1 = DisputeServiceResult1(
    success=False,
    error_message='errorMessage2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

