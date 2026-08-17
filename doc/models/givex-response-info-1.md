
# Givex Response Info 1

**givex** details

## Structure

`GivexResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_code` | `str` | Optional | The three-character ISO currency code |
| `password` | `str` | Optional | The password provided by the acquirer. |
| `payment_flow` | `str` | Optional | The sales channel used for the payment. |
| `username` | `str` | Optional | The username provided by the acquirer. |

## Example

```python
from adyen.models.givex_response_info_1 import GivexResponseInfo1

givex_response_info_1 = GivexResponseInfo1(
    currency_code='currencyCode6',
    password='password0',
    payment_flow='paymentFlow4',
    username='username6'
)
```

