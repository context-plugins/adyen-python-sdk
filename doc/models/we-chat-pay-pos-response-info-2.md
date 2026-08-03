
# We Chat Pay Pos Response Info 2

**wechatpay_pos** details

*This model accepts additional fields of type Any.*

## Structure

`WeChatPayPosResponseInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contact_person_name` | `str` | Optional | The name of the contact person from merchant support. |
| `email` | `str` | Optional | The email address of merchant support. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.we_chat_pay_pos_response_info_2 import WeChatPayPosResponseInfo2

we_chat_pay_pos_response_info_2 = WeChatPayPosResponseInfo2(
    contact_person_name='contactPersonName0',
    email='email0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

