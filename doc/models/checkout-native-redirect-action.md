
# Checkout Native Redirect Action

*This model accepts additional fields of type Any.*

## Structure

`CheckoutNativeRedirectAction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | `Dict[str, str]` | Optional | When the redirect URL must be accessed via POST, use this data to post to the redirect URL. |
| `method` | `str` | Optional | Specifies the HTTP method, for example GET or POST. |
| `native_redirect_data` | `str` | Optional | Native SDK's redirect data containing the direct issuer link and state data that must be submitted to the /v1/nativeRedirect/redirectResult. |
| `payment_method_type` | `str` | Optional | Specifies the payment method. |
| `mtype` | [`Type553`](../../doc/models/type-553.md) | Required | **nativeRedirect** |
| `url` | `str` | Optional | Specifies the URL to redirect to. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.checkout_native_redirect_action import CheckoutNativeRedirectAction
from adyen.models.type_553 import Type553

checkout_native_redirect_action = CheckoutNativeRedirectAction(
    mtype=Type553.NATIVEREDIRECT,
    data={
        'key0': 'data7',
        'key1': 'data8',
        'key2': 'data9'
    },
    method='method4',
    native_redirect_data='nativeRedirectData6',
    payment_method_type='paymentMethodType4',
    url='url6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

