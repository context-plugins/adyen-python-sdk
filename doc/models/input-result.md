
# Input Result

*This model accepts additional fields of type Any.*

## Structure

`InputResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device` | [`Device4`](../../doc/models/device-4.md) | Required | - |
| `info_qualify` | [`InfoQualify2`](../../doc/models/info-qualify-2.md) | Required | - |
| `response` | [`Response3`](../../doc/models/response-3.md) | Required | - |
| `input` | [`Input`](../../doc/models/input.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.device_4 import Device4
from adyen.models.error_condition_1 import ErrorCondition1
from adyen.models.info_qualify_2 import InfoQualify2
from adyen.models.input import Input
from adyen.models.input_command_1 import InputCommand1
from adyen.models.input_result import InputResult
from adyen.models.response_3 import Response3
from adyen.models.result_11 import Result11

input_result = InputResult(
    device=Device4.CASHIERDISPLAY,
    info_qualify=InfoQualify2.STATUS,
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
)
```

