
# Checkout Sdk Action

*This model accepts additional fields of type Any.*

## Structure

`CheckoutSdkAction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_data` | `str` | Optional | Encoded payment data. |
| `payment_method_type` | `str` | Optional | Specifies the payment method. |
| `sdk_data` | `Dict[str, str]` | Optional | The data to pass to the SDK. |
| `mtype` | [`Type19`](../../doc/models/type-19.md) | Required | - |
| `url` | `str` | Optional | Specifies the URL to redirect to. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.checkout_sdk_action import CheckoutSdkAction
from adyen.models.type_19 import Type19

checkout_sdk_action = CheckoutSdkAction(
    mtype=Type19.SDK,
    payment_data='paymentData2',
    payment_method_type='paymentMethodType2',
    sdk_data={
        'key0': 'sdkData5',
        'key1': 'sdkData6',
        'key2': 'sdkData7'
    },
    url='url4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

