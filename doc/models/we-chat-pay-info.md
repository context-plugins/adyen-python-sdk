
# We Chat Pay Info

## Structure

`WeChatPayInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contact_person_name` | `str` | Required | The name of the contact person from merchant support. |
| `email` | `str` | Required | The email address of merchant support. |

## Example

```python
from adyen.models.we_chat_pay_info import WeChatPayInfo

we_chat_pay_info = WeChatPayInfo(
    contact_person_name='contactPersonName6',
    email='email4'
)
```

