
# Response 11

Result of a message request processing.

*This model accepts additional fields of type Any.*

## Structure

`Response11`

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
from adyen.models.response_11 import Response11
from adyen.models.result_11 import Result11

response_11 = Response11(
    result=Result11.FAILURE,
    error_condition=ErrorCondition1.DEVICEOUT,
    additional_response='AdditionalResponse6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

