
# Pay Me Info

## Structure

`PayMeInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_name` | `str` | Required | Merchant display name |
| `logo` | `str` | Required | Merchant logo. Format: Base64-encoded string. |
| `support_email` | `str` | Required | The email address of merchant support. |

## Example

```python
from adyen.models.pay_me_info import PayMeInfo

pay_me_info = PayMeInfo(
    display_name='displayName4',
    logo='logo4',
    support_email='supportEmail4'
)
```

