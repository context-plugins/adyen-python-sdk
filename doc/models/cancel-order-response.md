
# Cancel Order Response

## Structure

`CancelOrderResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `psp_reference` | `str` | Required | A unique reference of the cancellation request. |
| `result_code` | `str` | Required, Constant | The result of the cancellation request.<br><br>Possible values:<br><br>* **Received** – Indicates the cancellation has successfully been received by Adyen, and will be processed.<br><br>**Value**: `"Received"` |

## Example

```python
from adyen.models.cancel_order_response import CancelOrderResponse

cancel_order_response = CancelOrderResponse(
    psp_reference='pspReference6'
)
```

