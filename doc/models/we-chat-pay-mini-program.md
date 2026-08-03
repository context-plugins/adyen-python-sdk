
# We Chat Pay Mini Program

*This model accepts additional fields of type Any.*

## Structure

`WeChatPayMiniProgram`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `app_id` | `str` | Optional | - |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `openid` | `str` | Optional | - |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `mtype` | [`Type57`](../../doc/models/type-57.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.we_chat_pay_mini_program import WeChatPayMiniProgram

we_chat_pay_mini_program = WeChatPayMiniProgram(
    app_id='appId2',
    checkout_attempt_id='checkoutAttemptId2',
    openid='openid4',
    recurring_detail_reference='recurringDetailReference6',
    sdk_data='sdkData4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

