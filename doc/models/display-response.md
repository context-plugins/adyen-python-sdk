
# Display Response

It conveys the result of the display, parallel to the message request, except if response not required and absent.
Content of the Display Response message.

*This model accepts additional fields of type Any.*

## Structure

`DisplayResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `output_result` | [`List[OutputResult]`](../../doc/models/output-result.md) | Required | Information related to the result the output (display, print, input).<br>One per DisplayOutput item of the request, and in the same order. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.device_3 import Device3
from adyen.models.display_response import DisplayResponse
from adyen.models.error_condition_1 import ErrorCondition1
from adyen.models.info_qualify_3 import InfoQualify3
from adyen.models.output_result import OutputResult
from adyen.models.response_3 import Response3
from adyen.models.result_11 import Result11

display_response = DisplayResponse(
    output_result=[
        OutputResult(
            device=Device3.CASHIERINPUT,
            info_qualify=InfoQualify3.DOCUMENT,
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
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

