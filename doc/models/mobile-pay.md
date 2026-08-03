
# Mobile Pay

*This model accepts additional fields of type Any.*

## Structure

`MobilePay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type37`](../../doc/models/type-37.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.mobile_pay import MobilePay
from adyen.models.type_37 import Type37

mobile_pay = MobilePay(
    checkout_attempt_id='checkoutAttemptId4',
    sdk_data='sdkData2',
    mtype=Type37.MOBILEPAY,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

