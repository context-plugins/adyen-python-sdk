
# Pay Me Info

*This model accepts additional fields of type Any.*

## Structure

`PayMeInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_name` | `str` | Required | Merchant display name |
| `logo` | `str` | Required | Merchant logo. Format: Base64-encoded string. |
| `support_email` | `str` | Required | The email address of merchant support. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.pay_me_info import PayMeInfo

pay_me_info = PayMeInfo(
    display_name='displayName4',
    logo='logo4',
    support_email='supportEmail4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

