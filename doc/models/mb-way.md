
# Mb Way

*This model accepts additional fields of type Any.*

## Structure

`MbWay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `shopper_email` | `str` | Required | - |
| `telephone_number` | `str` | Required | - |
| `mtype` | [`Type36`](../../doc/models/type-36.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.mb_way import MbWay
from adyen.models.type_36 import Type36

mb_way = MbWay(
    shopper_email='shopperEmail2',
    telephone_number='telephoneNumber6',
    checkout_attempt_id='checkoutAttemptId0',
    sdk_data='sdkData6',
    mtype=Type36.MBWAY,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

