
# Checkout Await Action

*This model accepts additional fields of type Any.*

## Structure

`CheckoutAwaitAction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_data` | `str` | Optional | Encoded payment data. |
| `payment_method_type` | `str` | Optional | Specifies the payment method. |
| `mtype` | [`Type493`](../../doc/models/type-493.md) | Required | **await** |
| `url` | `str` | Optional | Specifies the URL to redirect to. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.checkout_await_action import CheckoutAwaitAction
from adyen.models.type_493 import Type493

checkout_await_action = CheckoutAwaitAction(
    mtype=Type493.AWAIT,
    payment_data='paymentData0',
    payment_method_type='paymentMethodType0',
    url='url2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

