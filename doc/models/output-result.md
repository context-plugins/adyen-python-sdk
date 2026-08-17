
# Output Result

In the message response, it contains the result of the output, if required in the message request.
Information related to the result the output (display, print, input).

## Structure

`OutputResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device` | [`Device3Enum`](../../doc/models/device-3-enum.md) | Required | Logical device located on a Sale Terminal or a POI Terminal, in term of class of information to output (display, print or store), or input (keyboard) for the Cashier or the Customer.<br>Copy.<br>Possible values:<br><br>* **CashierDisplay**<br>* **CashierInput**<br>* **CustomerDisplay**<br>* **CustomerInput** |
| `info_qualify` | [`InfoQualify3Enum`](../../doc/models/info-qualify-3-enum.md) | Required | Qualification of the information to sent to an output logical device, to display or print to the Cashier or the Customer.<br>Copy.<br>Possible values:<br><br>* **CustomerAssistance**<br>* **Display**<br>* **Document**<br>* **Error**<br>* **Input**<br>* **POIReplication**<br>* **Receipt**<br>* **Sound**<br>* **Status**<br>* **Voucher** |
| `response` | [`Response11`](../../doc/models/response-11.md) | Required | Result of a message request processing. |

## Example

```python
from adyen.models.device_3_enum import Device3Enum
from adyen.models.error_condition_1_enum import ErrorCondition1Enum
from adyen.models.info_qualify_3_enum import InfoQualify3Enum
from adyen.models.output_result import OutputResult
from adyen.models.response_11 import Response11
from adyen.models.result_11_enum import Result11Enum

output_result = OutputResult(
    device=Device3Enum.CASHIERINPUT,
    info_qualify=InfoQualify3Enum.STATUS,
    response=Response11(
        result=Result11Enum.PARTIAL,
        error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
        additional_response='AdditionalResponse8'
    )
)
```

