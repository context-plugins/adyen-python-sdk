
# Pay Pal Response Info

## Structure

`PayPalResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `direct_capture` | `bool` | Optional | Indicates if direct (immediate) capture for PayPal is enabled. If set to **true**, this setting overrides the [capture](https://docs.adyen.com/online-payments/capture) settings of your merchant account. Default value: **true**. |
| `payer_id` | `str` | Optional | PayPal Merchant ID. Character length and limitations: 13 single-byte alphanumeric characters.<br><br>**Constraints**: *Minimum Length*: `13`, *Maximum Length*: `13` |
| `subject` | `str` | Optional | Your business email address. |

## Example

```python
from adyen.models.pay_pal_response_info import PayPalResponseInfo

pay_pal_response_info = PayPalResponseInfo(
    direct_capture=False,
    payer_id='payerId4',
    subject='subject2'
)
```

