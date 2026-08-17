
# We Chat Pay

## Structure

`WeChatPay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type56Enum`](../../doc/models/type-56-enum.md) | Optional | **wechatpay**<br><br>**Default**: `"wechatpay"` |

## Example

```python
from adyen.models.type_56_enum import Type56Enum
from adyen.models.we_chat_pay import WeChatPay

we_chat_pay = WeChatPay(
    checkout_attempt_id='checkoutAttemptId4',
    sdk_data='sdkData2',
    mtype=Type56Enum.WECHATPAY
)
```

