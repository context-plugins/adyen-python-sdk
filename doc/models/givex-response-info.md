
# Givex Response Info

## Structure

`GivexResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_code` | `str` | Optional | The three-character ISO currency code |
| `password` | `str` | Optional | The password provided by the acquirer. |
| `payment_flow` | `str` | Optional | The sales channel used for the payment. |
| `username` | `str` | Optional | The username provided by the acquirer. |

## Example

```python
from adyen.models.givex_response_info import GivexResponseInfo

givex_response_info = GivexResponseInfo(
    currency_code='currencyCode0',
    password='password4',
    payment_flow='paymentFlow8',
    username='username0'
)
```

