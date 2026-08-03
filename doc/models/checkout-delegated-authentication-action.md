
# Checkout Delegated Authentication Action

*This model accepts additional fields of type Any.*

## Structure

`CheckoutDelegatedAuthenticationAction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorisation_token` | `str` | Optional | A token needed to authorise a payment. |
| `payment_data` | `str` | Optional | Encoded payment data. |
| `payment_method_type` | `str` | Optional | Specifies the payment method. |
| `token` | `str` | Optional | A token to pass to the delegatedAuthentication component. |
| `mtype` | [`Type543`](../../doc/models/type-543.md) | Required | **delegatedAuthentication** |
| `url` | `str` | Optional | Specifies the URL to redirect to. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.checkout_delegated_authentication_action import CheckoutDelegatedAuthenticationAction
from adyen.models.type_543 import Type543

checkout_delegated_authentication_action = CheckoutDelegatedAuthenticationAction(
    mtype=Type543.DELEGATEDAUTHENTICATION,
    authorisation_token='authorisationToken8',
    payment_data='paymentData6',
    payment_method_type='paymentMethodType6',
    token='token8',
    url='url8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

