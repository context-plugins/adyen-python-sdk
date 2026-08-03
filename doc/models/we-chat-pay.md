
# We Chat Pay

*This model accepts additional fields of type Any.*

## Structure

`WeChatPay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type56`](../../doc/models/type-56.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.type_56 import Type56
from adyen.models.we_chat_pay import WeChatPay

we_chat_pay = WeChatPay(
    checkout_attempt_id='checkoutAttemptId4',
    sdk_data='sdkData2',
    mtype=Type56.WECHATPAY,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

