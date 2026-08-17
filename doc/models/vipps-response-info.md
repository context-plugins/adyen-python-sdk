
# Vipps Response Info

## Structure

`VippsResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `logo` | `str` | Optional | Vipps logo. Format: Base64-encoded string. |
| `subscription_cancel_url` | `str` | Optional | Vipps subscription cancel url (required in case of [recurring payments](https://docs.adyen.com/online-payments/tokenization)) |

## Example

```python
from adyen.models.vipps_response_info import VippsResponseInfo

vipps_response_info = VippsResponseInfo(
    logo='logo4',
    subscription_cancel_url='subscriptionCancelUrl2'
)
```

