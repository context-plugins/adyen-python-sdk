
# We Chat Pay Pos Response Info 2

**wechatpay_pos** details

## Structure

`WeChatPayPosResponseInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contact_person_name` | `str` | Optional | The name of the contact person from merchant support. |
| `email` | `str` | Optional | The email address of merchant support. |

## Example

```python
from adyen.models.we_chat_pay_pos_response_info_2 import WeChatPayPosResponseInfo2

we_chat_pay_pos_response_info_2 = WeChatPayPosResponseInfo2(
    contact_person_name='contactPersonName0',
    email='email0'
)
```

