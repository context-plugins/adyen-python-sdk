
# Checkout Redirect Action

*This model accepts additional fields of type Any.*

## Structure

`CheckoutRedirectAction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | `Dict[str, str]` | Optional | When the redirect URL must be accessed via POST, use this data to post to the redirect URL. |
| `method` | `str` | Optional | Specifies the HTTP method, for example GET or POST. |
| `payment_method_type` | `str` | Optional | Specifies the payment method. |
| `mtype` | [`Type573`](../../doc/models/type-573.md) | Required | **redirect** |
| `url` | `str` | Optional | Specifies the URL to redirect to. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.checkout_redirect_action import CheckoutRedirectAction
from adyen.models.type_573 import Type573

checkout_redirect_action = CheckoutRedirectAction(
    mtype=Type573.REDIRECT,
    data={
        'key0': 'data7'
    },
    method='method4',
    payment_method_type='paymentMethodType6',
    url='url6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

