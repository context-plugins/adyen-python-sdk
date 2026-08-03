
# Response 1

Result of a message request processing.
If Result is Success, `ErrorCondition` is absent or not used in the processing of the message. In the other cases, the `ErrorCondition` has to be present and can refine the processing of the message response. `AdditionalResponse` gives more information about the success or the failure of the message request processing, for logging without real time involvements.

*This model accepts additional fields of type Any.*

## Structure

`Response1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `result` | [`Result11`](../../doc/models/result-11.md) | Required | - |
| `error_condition` | [`ErrorCondition1`](../../doc/models/error-condition-1.md) | Optional | - |
| `additional_response` | `str` | Optional | Additional information related to processing status of a message request.<br>If present, the POI logs it for further examination.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.error_condition_1 import ErrorCondition1
from adyen.models.response_1 import Response1
from adyen.models.result_11 import Result11

response_1 = Response1(
    result=Result11.PARTIAL,
    error_condition=ErrorCondition1.LOGGEDOUT,
    additional_response='AdditionalResponse0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

