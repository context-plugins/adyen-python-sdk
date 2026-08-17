
# Pay Me Response Info 1

**payme** details

## Structure

`PayMeResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_name` | `str` | Optional | Merchant display name |
| `logo` | `str` | Optional | Merchant logo. Format: Base64-encoded string. |
| `support_email` | `str` | Optional | The email address of merchant support. |

## Example

```python
from adyen.models.pay_me_response_info_1 import PayMeResponseInfo1

pay_me_response_info_1 = PayMeResponseInfo1(
    display_name='displayName2',
    logo='logo6',
    support_email='supportEmail6'
)
```

