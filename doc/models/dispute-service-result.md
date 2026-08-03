
# Dispute Service Result

*This model accepts additional fields of type Any.*

## Structure

`DisputeServiceResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `str` | Optional | The general error message. |
| `success` | `bool` | Required | Indicates whether the request succeeded. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.dispute_service_result import DisputeServiceResult

dispute_service_result = DisputeServiceResult(
    success=False,
    error_message='errorMessage2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

