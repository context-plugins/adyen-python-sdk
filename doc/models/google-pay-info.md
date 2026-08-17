
# Google Pay Info

## Structure

`GooglePayInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Required | Google Pay [Merchant ID](https://support.google.com/paymentscenter/answer/7163092?hl=en). Character length and limitations: 16 alphanumeric characters or 20 numeric characters.<br><br>**Constraints**: *Minimum Length*: `16`, *Maximum Length*: `20` |
| `reuse_merchant_id` | `bool` | Optional | Indicates whether the Google Pay Merchant ID is used for several merchant accounts. Default value: **false**. |

## Example

```python
from adyen.models.google_pay_info import GooglePayInfo

google_pay_info = GooglePayInfo(
    merchant_id='merchantId4',
    reuse_merchant_id=False
)
```

