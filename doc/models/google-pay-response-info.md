
# Google Pay Response Info

## Structure

`GooglePayResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Optional | Google Pay [Merchant ID] |
| `reuse_merchant_id` | `bool` | Optional | Indicates whether the Google Pay Merchant ID is used for several merchant accounts. |

## Example

```python
from adyen.models.google_pay_response_info import GooglePayResponseInfo

google_pay_response_info = GooglePayResponseInfo(
    merchant_id='merchantId0',
    reuse_merchant_id=False
)
```

