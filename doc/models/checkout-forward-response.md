
# Checkout Forward Response

*This model accepts additional fields of type Any.*

## Structure

`CheckoutForwardResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_reference` | `str` | Optional | Merchant defined payment reference. |
| `psp_reference` | `str` | Optional | Adyen's 16-character reference associated with the transaction/request. This value is globally unique. Use this reference when you communicate with us about this request. |
| `response` | [`CheckoutForwardResponseFromUrl`](../../doc/models/checkout-forward-response-from-url.md) | Required | - |
| `stored_payment_method_id` | `str` | Optional | The unique identifier of the token. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.checkout_forward_response import CheckoutForwardResponse
from adyen.models.checkout_forward_response_from_url import CheckoutForwardResponseFromUrl

checkout_forward_response = CheckoutForwardResponse(
    response=CheckoutForwardResponseFromUrl(
        body='body6',
        headers={
            'key0': 'headers3',
            'key1': 'headers4',
            'key2': 'headers5'
        },
        status=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    merchant_reference='merchantReference8',
    psp_reference='pspReference0',
    stored_payment_method_id='storedPaymentMethodId2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

