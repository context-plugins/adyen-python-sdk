
# Android Pay

*This model accepts additional fields of type Any.*

## Structure

`AndroidPay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type61`](../../doc/models/type-61.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.android_pay import AndroidPay
from adyen.models.type_61 import Type61

android_pay = AndroidPay(
    checkout_attempt_id='checkoutAttemptId8',
    sdk_data='sdkData8',
    mtype=Type61.ANDROIDPAY,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

