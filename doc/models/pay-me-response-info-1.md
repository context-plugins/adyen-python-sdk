
# Pay Me Response Info 1

**payme** details

*This model accepts additional fields of type Any.*

## Structure

`PayMeResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_name` | `str` | Optional | Merchant display name |
| `logo` | `str` | Optional | Merchant logo. Format: Base64-encoded string. |
| `support_email` | `str` | Optional | The email address of merchant support. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.pay_me_response_info_1 import PayMeResponseInfo1

pay_me_response_info_1 = PayMeResponseInfo1(
    display_name='displayName2',
    logo='logo6',
    support_email='supportEmail6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

