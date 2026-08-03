
# Alma

*This model accepts additional fields of type Any.*

## Structure

`Alma`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `fee_type` | [`FeeType`](../../doc/models/fee-type.md) | Optional | - |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type31`](../../doc/models/type-31.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.alma import Alma
from adyen.models.fee_type import FeeType
from adyen.models.type_31 import Type31

alma = Alma(
    checkout_attempt_id='checkoutAttemptId2',
    fee_type=FeeType.MERCHANTPAYS,
    sdk_data='sdkData4',
    mtype=Type31.ALMA,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

