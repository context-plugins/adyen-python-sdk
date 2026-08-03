
# Input Response 3

*This model accepts additional fields of type Any.*

## Structure

`InputResponse3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `output_result` | [`OutputResult2`](../../doc/models/output-result-2.md) | Optional | - |
| `input_result` | [`InputResult`](../../doc/models/input-result.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.device_3 import Device3
from adyen.models.device_4 import Device4
from adyen.models.error_condition_1 import ErrorCondition1
from adyen.models.info_qualify_2 import InfoQualify2
from adyen.models.info_qualify_3 import InfoQualify3
from adyen.models.input import Input
from adyen.models.input_command_1 import InputCommand1
from adyen.models.input_response_3 import InputResponse3
from adyen.models.input_result import InputResult
from adyen.models.output_result_2 import OutputResult2
from adyen.models.response_3 import Response3
from adyen.models.result_11 import Result11

input_response_3 = InputResponse3(
    input_result=InputResult(
        device=Device4.CASHIERDISPLAY,
        info_qualify=InfoQualify2.INPUT,
        response=Response3(
            result=Result11.PARTIAL,
            error_condition=ErrorCondition1.PAYMENTRESTRICTION,
            additional_response='AdditionalResponse8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        input=Input(
            input_command=InputCommand1.GETMENUENTRY,
            confirmed_flag=False,
            function_key=134,
            text_input='TextInput4',
            digit_input=152,
            password='Password0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    output_result=OutputResult2(
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
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

