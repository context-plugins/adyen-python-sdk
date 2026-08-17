
# Checkout Redirect Action

## Structure

`CheckoutRedirectAction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | `Dict[str, str]` | Optional | When the redirect URL must be accessed via POST, use this data to post to the redirect URL. |
| `method` | `str` | Optional | Specifies the HTTP method, for example GET or POST. |
| `payment_method_type` | `str` | Optional | Specifies the payment method. |
| `mtype` | `str` | Required, Constant | **redirect**<br><br>**Value**: `"redirect"` |
| `url` | `str` | Optional | Specifies the URL to redirect to. |

## Example

```python
from adyen.models.checkout_redirect_action import CheckoutRedirectAction

checkout_redirect_action = CheckoutRedirectAction(
    data={
        'key0': 'data7'
    },
    method='method4',
    payment_method_type='paymentMethodType6',
    url='url6'
)
```

