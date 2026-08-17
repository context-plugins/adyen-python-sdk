
# We Chat Pay Pos Info

## Structure

`WeChatPayPosInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contact_person_name` | `str` | Required | The name of the contact person from merchant support. |
| `email` | `str` | Required | The email address of merchant support. |

## Example

```python
from adyen.models.we_chat_pay_pos_info import WeChatPayPosInfo

we_chat_pay_pos_info = WeChatPayPosInfo(
    contact_person_name='contactPersonName6',
    email='email4'
)
```

