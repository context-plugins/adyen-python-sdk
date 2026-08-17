
# Display Response 2

Content of the Display Response message.

## Structure

`DisplayResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `output_result` | [`List[OutputResult]`](../../doc/models/output-result.md) | Required | Information related to the result the output (display, print, input).<br>One per DisplayOutput item of the request, and in the same order. |

## Example

```python
from adyen.models.device_3_enum import Device3Enum
from adyen.models.display_response_2 import DisplayResponse2
from adyen.models.error_condition_1_enum import ErrorCondition1Enum
from adyen.models.info_qualify_3_enum import InfoQualify3Enum
from adyen.models.output_result import OutputResult
from adyen.models.response_11 import Response11
from adyen.models.result_11_enum import Result11Enum

display_response_2 = DisplayResponse2(
    output_result=[
        OutputResult(
            device=Device3Enum.CASHIERINPUT,
            info_qualify=InfoQualify3Enum.DOCUMENT,
            response=Response11(
                result=Result11Enum.PARTIAL,
                error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
                additional_response='AdditionalResponse8'
            )
        )
    ]
)
```

