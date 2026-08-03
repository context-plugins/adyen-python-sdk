
# Pay Me Info 1

Details to provide if `type` is **payme**.

*This model accepts additional fields of type Any.*

## Structure

`PayMeInfo1`

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

from adyen.models.pay_me_info_1 import PayMeInfo1

pay_me_info_1 = PayMeInfo1(
    display_name='displayName0',
    logo='logo2',
    support_email='supportEmail8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

