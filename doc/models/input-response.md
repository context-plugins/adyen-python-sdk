
# Input Response

It conveys the result of the input or the result of the outputs, parallel to the message request, except if response not required and absent.
Content of the Input Response message.

## Structure

`InputResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `output_result` | [`OutputResult1`](../../doc/models/output-result-1.md) | Optional | Information related to the result the output (display, print, input).<br>If DisplayOutput present in the request. |
| `input_result` | [`InputResult2`](../../doc/models/input-result-2.md) | Required | Contains the result and the content of the input. |

## Example

```python
from adyen.models.device_3_enum import Device3Enum
from adyen.models.device_4_enum import Device4Enum
from adyen.models.error_condition_1_enum import ErrorCondition1Enum
from adyen.models.info_qualify_2_enum import InfoQualify2Enum
from adyen.models.info_qualify_3_enum import InfoQualify3Enum
from adyen.models.input_2 import Input2
from adyen.models.input_command_1_enum import InputCommand1Enum
from adyen.models.input_response import InputResponse
from adyen.models.input_result_2 import InputResult2
from adyen.models.output_result_1 import OutputResult1
from adyen.models.response_1 import Response1
from adyen.models.response_11 import Response11
from adyen.models.result_11_enum import Result11Enum

input_response = InputResponse(
    input_result=InputResult2(
        device=Device4Enum.CASHIERDISPLAY,
        info_qualify=InfoQualify2Enum.INPUT,
        response=Response1(
            result=Result11Enum.PARTIAL,
            error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
            additional_response='AdditionalResponse8'
        ),
        input=Input2(
            input_command=InputCommand1Enum.GETMENUENTRY,
            confirmed_flag=False,
            function_key=134,
            text_input='TextInput4',
            digit_input=152,
            password='Password0'
        )
    ),
    output_result=OutputResult1(
        device=Device3Enum.CASHIERINPUT,
        info_qualify=InfoQualify3Enum.DOCUMENT,
        response=Response11(
            result=Result11Enum.PARTIAL,
            error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
            additional_response='AdditionalResponse8'
        )
    )
)
```

