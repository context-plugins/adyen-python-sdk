
# We Chat Pay Response Info 2

**wechatpay** details

## Structure

`WeChatPayResponseInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contact_person_name` | `str` | Optional | The name of the contact person from merchant support. |
| `email` | `str` | Optional | The email address of merchant support. |

## Example

```python
from adyen.models.we_chat_pay_response_info_2 import WeChatPayResponseInfo2

we_chat_pay_response_info_2 = WeChatPayResponseInfo2(
    contact_person_name='contactPersonName8',
    email='email2'
)
```

