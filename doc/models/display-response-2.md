
# Display Response 2

Content of the Display Response message.

*This model accepts additional fields of type Any.*

## Structure

`DisplayResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `output_result` | [`List[OutputResult]`](../../doc/models/output-result.md) | Required | Information related to the result the output (display, print, input).<br>One per DisplayOutput item of the request, and in the same order. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.device_3 import Device3
from adyen.models.display_response_2 import DisplayResponse2
from adyen.models.error_condition_1 import ErrorCondition1
from adyen.models.info_qualify_3 import InfoQualify3
from adyen.models.output_result import OutputResult
from adyen.models.response_3 import Response3
from adyen.models.result_11 import Result11

display_response_2 = DisplayResponse2(
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

