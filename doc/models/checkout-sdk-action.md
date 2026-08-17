
# Checkout SDK Action

## Structure

`CheckoutSDKAction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_data` | `str` | Optional | Encoded payment data. |
| `payment_method_type` | `str` | Optional | Specifies the payment method. |
| `sdk_data` | `Dict[str, str]` | Optional | The data to pass to the SDK. |
| `mtype` | [`Type19Enum`](../../doc/models/type-19-enum.md) | Required | The type of the action. |
| `url` | `str` | Optional | Specifies the URL to redirect to. |

## Example

```python
from adyen.models.checkout_sdk_action import CheckoutSDKAction
from adyen.models.type_19_enum import Type19Enum

checkout_sdk_action = CheckoutSDKAction(
    mtype=Type19Enum.SDK,
    payment_data='paymentData2',
    payment_method_type='paymentMethodType2',
    sdk_data={
        'key0': 'sdkData5',
        'key1': 'sdkData6',
        'key2': 'sdkData7'
    },
    url='url4'
)
```

