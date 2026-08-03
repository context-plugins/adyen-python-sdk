
# Affirm

*This model accepts additional fields of type Any.*

## Structure

`Affirm`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type12`](../../doc/models/type-12.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.affirm import Affirm
from adyen.models.type_12 import Type12

affirm = Affirm(
    checkout_attempt_id='checkoutAttemptId2',
    sdk_data='sdkData4',
    mtype=Type12.AFFIRM,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

