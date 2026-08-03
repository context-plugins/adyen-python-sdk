
# Doku

*This model accepts additional fields of type Any.*

## Structure

`Doku`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `first_name` | `str` | Required | The shopper's first name. |
| `last_name` | `str` | Required | The shopper's last name. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `shopper_email` | `str` | Required | The shopper's email. |
| `mtype` | [`Type23`](../../doc/models/type-23.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.doku import Doku
from adyen.models.type_23 import Type23

doku = Doku(
    first_name='firstName8',
    last_name='lastName0',
    shopper_email='shopperEmail0',
    mtype=Type23.DOKU_OVO,
    checkout_attempt_id='checkoutAttemptId2',
    sdk_data='sdkData4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

