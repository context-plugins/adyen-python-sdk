
# Logout Response 2

Content of the Logout Response message.

*This model accepts additional fields of type Any.*

## Structure

`LogoutResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response3`](../../doc/models/response-3.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.error_condition_1 import ErrorCondition1
from adyen.models.logout_response_2 import LogoutResponse2
from adyen.models.response_3 import Response3
from adyen.models.result_11 import Result11

logout_response_2 = LogoutResponse2(
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

