
# Checkout Forward Response

## Structure

`CheckoutForwardResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_reference` | `str` | Optional | Merchant defined payment reference. |
| `psp_reference` | `str` | Optional | Adyen's 16-character reference associated with the transaction/request. This value is globally unique. Use this reference when you communicate with us about this request. |
| `response` | [`CheckoutForwardResponseFromUrl2`](../../doc/models/checkout-forward-response-from-url-2.md) | Required | The details of the response Adyen received from the third party. |
| `stored_payment_method_id` | `str` | Optional | The unique identifier of the token. |

## Example

```python
from adyen.models.checkout_forward_response import CheckoutForwardResponse
from adyen.models.checkout_forward_response_from_url_2 import CheckoutForwardResponseFromUrl2

checkout_forward_response = CheckoutForwardResponse(
    response=CheckoutForwardResponseFromUrl2(
        body='body6',
        headers={
            'key0': 'headers3',
            'key1': 'headers4',
            'key2': 'headers5'
        },
        status=110
    ),
    merchant_reference='merchantReference8',
    psp_reference='pspReference0',
    stored_payment_method_id='storedPaymentMethodId2'
)
```

