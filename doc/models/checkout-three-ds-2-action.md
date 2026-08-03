
# Checkout Three Ds 2 Action

*This model accepts additional fields of type Any.*

## Structure

`CheckoutThreeDs2Action`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorisation_token` | `str` | Optional | A token needed to authorise a payment. |
| `payment_data` | `str` | Optional | Encoded payment data. |
| `payment_method_type` | `str` | Optional | Specifies the payment method. |
| `subtype` | `str` | Optional | A subtype of the token. |
| `token` | `str` | Optional | A token to pass to the 3DS2 Component to get the fingerprint. |
| `mtype` | [`Type583`](../../doc/models/type-583.md) | Required | **threeDS2** |
| `url` | `str` | Optional | Specifies the URL to redirect to. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.checkout_three_ds_2_action import CheckoutThreeDs2Action
from adyen.models.type_583 import Type583

checkout_three_ds_2_action = CheckoutThreeDs2Action(
    mtype=Type583.THREEDS2,
    authorisation_token='authorisationToken2',
    payment_data='paymentData0',
    payment_method_type='paymentMethodType0',
    subtype='subtype0',
    token='token8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

