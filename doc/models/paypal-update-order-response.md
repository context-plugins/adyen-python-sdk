
# Paypal Update Order Response

## Structure

`PaypalUpdateOrderResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_data` | `str` | Required | The updated paymentData. |
| `status` | [`Status4Enum`](../../doc/models/status-4-enum.md) | Required | The status of the request. This indicates whether the order was successfully updated with PayPal. |

## Example

```python
from adyen.models.paypal_update_order_response import PaypalUpdateOrderResponse
from adyen.models.status_4_enum import Status4Enum

paypal_update_order_response = PaypalUpdateOrderResponse(
    payment_data='paymentData2',
    status=Status4Enum.ERROR
)
```

