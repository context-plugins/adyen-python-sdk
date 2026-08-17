
# We Chat Pay Response Info

## Structure

`WeChatPayResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contact_person_name` | `str` | Optional | The name of the contact person from merchant support. |
| `email` | `str` | Optional | The email address of merchant support. |

## Example

```python
from adyen.models.we_chat_pay_response_info import WeChatPayResponseInfo

we_chat_pay_response_info = WeChatPayResponseInfo(
    contact_person_name='contactPersonName0',
    email='email0'
)
```

