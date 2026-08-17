
# We Chat Pay Pos Info 2

Details to provide if `type` is **wechatpay_pos**.

## Structure

`WeChatPayPosInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contact_person_name` | `str` | Required | The name of the contact person from merchant support. |
| `email` | `str` | Required | The email address of merchant support. |

## Example

```python
from adyen.models.we_chat_pay_pos_info_2 import WeChatPayPosInfo2

we_chat_pay_pos_info_2 = WeChatPayPosInfo2(
    contact_person_name='contactPersonName0',
    email='email0'
)
```

