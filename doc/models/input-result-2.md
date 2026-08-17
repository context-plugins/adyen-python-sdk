
# Input Result 2

Contains the result and the content of the input.

## Structure

`InputResult2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device` | [`Device4Enum`](../../doc/models/device-4-enum.md) | Required | Logical device located on a Sale Terminal or a POI Terminal, in terms of class of information to output (display, print or store), or input (keyboard) for the Cashier or the Customer.<br>Possible values:<br><br>* **CashierDisplay**<br>* **CashierInput**<br>* **CustomerDisplay**<br>* **CustomerInput** |
| `info_qualify` | [`InfoQualify2Enum`](../../doc/models/info-qualify-2-enum.md) | Required | Qualification of the information to send to an output logical device, to display or print to the Cashier or the Customer.<br>Possible values:<br><br>* **CustomerAssistance**<br>* **Display**<br>* **Document**<br>* **Error**<br>* **Input**<br>* **POIReplication**<br>* **Receipt**<br>* **Sound**<br>* **Status**<br>* **Voucher** |
| `response` | [`Response1`](../../doc/models/response-1.md) | Required | Result of a message request processing.<br>If Result is Success, `ErrorCondition` is absent or not used in the processing of the message. In the other cases, the `ErrorCondition` has to be present and can refine the processing of the message response. `AdditionalResponse` gives more information about the success or the failure of the message request processing, for logging without real time involvements. |
| `input` | [`Input2`](../../doc/models/input-2.md) | Optional | Data entered by the user, related to the input command. |

## Example

```python
from adyen.models.device_4_enum import Device4Enum
from adyen.models.error_condition_1_enum import ErrorCondition1Enum
from adyen.models.info_qualify_2_enum import InfoQualify2Enum
from adyen.models.input_2 import Input2
from adyen.models.input_command_1_enum import InputCommand1Enum
from adyen.models.input_result_2 import InputResult2
from adyen.models.response_1 import Response1
from adyen.models.result_11_enum import Result11Enum

input_result_2 = InputResult2(
    device=Device4Enum.CASHIERINPUT,
    info_qualify=InfoQualify2Enum.STATUS,
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
)
```

