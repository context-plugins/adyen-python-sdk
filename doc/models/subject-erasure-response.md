
# Subject Erasure Response

*This model accepts additional fields of type Any.*

## Structure

`SubjectErasureResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `result` | [`Result2`](../../doc/models/result-2.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.result_2 import Result2
from adyen.models.subject_erasure_response import SubjectErasureResponse

subject_erasure_response = SubjectErasureResponse(
    result=Result2.PAYMENT_NOT_FOUND,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

