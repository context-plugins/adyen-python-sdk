
# Cancel Order Response

*This model accepts additional fields of type Any.*

## Structure

`CancelOrderResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `psp_reference` | `str` | Required | A unique reference of the cancellation request. |
| `result_code` | [`ResultCode18`](../../doc/models/result-code-18.md) | Required | The result of the cancellation request.<br><br>Possible values:<br><br>* **Received** – Indicates the cancellation has successfully been received by Adyen, and will be processed. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.cancel_order_response import CancelOrderResponse
from adyen.models.result_code_18 import ResultCode18

cancel_order_response = CancelOrderResponse(
    psp_reference='pspReference6',
    result_code=ResultCode18.RECEIVED,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

