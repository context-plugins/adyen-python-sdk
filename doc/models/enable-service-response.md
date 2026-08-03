
# Enable Service Response

It conveys the result of the Enable Service processing.
Content of the Enable Service Response message.

*This model accepts additional fields of type Any.*

## Structure

`EnableServiceResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response3`](../../doc/models/response-3.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.enable_service_response import EnableServiceResponse
from adyen.models.error_condition_1 import ErrorCondition1
from adyen.models.response_3 import Response3
from adyen.models.result_11 import Result11

enable_service_response = EnableServiceResponse(
    response=Response3(
        result=Result11.PARTIAL,
        error_condition=ErrorCondition1.PAYMENTRESTRICTION,
        additional_response='AdditionalResponse8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

