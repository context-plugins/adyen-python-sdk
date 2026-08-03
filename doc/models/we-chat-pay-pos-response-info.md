
# We Chat Pay Pos Response Info

*This model accepts additional fields of type Any.*

## Structure

`WeChatPayPosResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contact_person_name` | `str` | Optional | The name of the contact person from merchant support. |
| `email` | `str` | Optional | The email address of merchant support. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.we_chat_pay_pos_response_info import WeChatPayPosResponseInfo

we_chat_pay_pos_response_info = WeChatPayPosResponseInfo(
    contact_person_name='contactPersonName6',
    email='email4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

