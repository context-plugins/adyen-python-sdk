
# Checkout Await Action

## Structure

`CheckoutAwaitAction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_data` | `str` | Optional | Encoded payment data. |
| `payment_method_type` | `str` | Optional | Specifies the payment method. |
| `mtype` | `str` | Required, Constant | **await**<br><br>**Value**: `"await"` |
| `url` | `str` | Optional | Specifies the URL to redirect to. |

## Example

```python
from adyen.models.checkout_await_action import CheckoutAwaitAction

checkout_await_action = CheckoutAwaitAction(
    payment_data='paymentData0',
    payment_method_type='paymentMethodType0',
    url='url2'
)
```

