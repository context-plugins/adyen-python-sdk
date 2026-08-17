
# Vipps Response Info 2

**vipps** details

## Structure

`VippsResponseInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `logo` | `str` | Optional | Vipps logo. Format: Base64-encoded string. |
| `subscription_cancel_url` | `str` | Optional | Vipps subscription cancel url (required in case of [recurring payments](https://docs.adyen.com/online-payments/tokenization)) |

## Example

```python
from adyen.models.vipps_response_info_2 import VippsResponseInfo2

vipps_response_info_2 = VippsResponseInfo2(
    logo='logo4',
    subscription_cancel_url='subscriptionCancelUrl2'
)
```

