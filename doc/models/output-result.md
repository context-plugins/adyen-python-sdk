
# Output Result

In the message response, it contains the result of the output, if required in the message request.
Information related to the result the output (display, print, input).

*This model accepts additional fields of type Any.*

## Structure

`OutputResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device` | [`Device3`](../../doc/models/device-3.md) | Required | - |
| `info_qualify` | [`InfoQualify3`](../../doc/models/info-qualify-3.md) | Required | - |
| `response` | [`Response3`](../../doc/models/response-3.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.device_3 import Device3
from adyen.models.error_condition_1 import ErrorCondition1
from adyen.models.info_qualify_3 import InfoQualify3
from adyen.models.output_result import OutputResult
from adyen.models.response_3 import Response3
from adyen.models.result_11 import Result11

output_result = OutputResult(
    device=Device3.CASHIERINPUT,
    info_qualify=InfoQualify3.STATUS,
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

