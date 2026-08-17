
# Apple Pay Session Response

## Structure

`ApplePaySessionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | `str` | Required | Base64 encoded data you need to [complete the Apple Pay merchant validation](https://docs.adyen.com/payment-methods/apple-pay/api-only?tab=adyen-certificate-validation_1#complete-apple-pay-session-validation). |

## Example

```python
from adyen.models.apple_pay_session_response import ApplePaySessionResponse

apple_pay_session_response = ApplePaySessionResponse(
    data='data0'
)
```

