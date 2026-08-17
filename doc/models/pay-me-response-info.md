
# Pay Me Response Info

## Structure

`PayMeResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_name` | `str` | Optional | Merchant display name |
| `logo` | `str` | Optional | Merchant logo. Format: Base64-encoded string. |
| `support_email` | `str` | Optional | The email address of merchant support. |

## Example

```python
from adyen.models.pay_me_response_info import PayMeResponseInfo

pay_me_response_info = PayMeResponseInfo(
    display_name='displayName4',
    logo='logo4',
    support_email='supportEmail4'
)
```

