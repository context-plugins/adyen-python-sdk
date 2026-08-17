
# Apple Pay Session Request

## Structure

`ApplePaySessionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_name` | `str` | Required | This is the name that your shoppers will see in the Apple Pay interface.<br><br>The value returned as `configuration.merchantName` field from the [`/paymentMethods`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/paymentMethods) response.<br><br>**Constraints**: *Maximum Length*: `64` |
| `domain_name` | `str` | Required | The domain name you provided when you added Apple Pay in your Customer Area.<br><br>This must match the `window.location.hostname` of the web shop. |
| `merchant_identifier` | `str` | Required | Your merchant identifier registered with Apple Pay.<br><br>Use the value of the `configuration.merchantId` field from the [`/paymentMethods`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/paymentMethods) response. |

## Example

```python
from adyen.models.apple_pay_session_request import ApplePaySessionRequest

apple_pay_session_request = ApplePaySessionRequest(
    display_name='displayName0',
    domain_name='domainName6',
    merchant_identifier='merchantIdentifier6'
)
```

