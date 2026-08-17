
# Vipps Info

## Structure

`VippsInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `logo` | `str` | Required | Vipps logo. Format: Base64-encoded string. |
| `subscription_cancel_url` | `str` | Optional | Vipps subscription cancel url (required in case of [recurring payments](https://docs.adyen.com/online-payments/tokenization)) |

## Example

```python
from adyen.models.vipps_info import VippsInfo

vipps_info = VippsInfo(
    logo='logo2',
    subscription_cancel_url='subscriptionCancelUrl0'
)
```

