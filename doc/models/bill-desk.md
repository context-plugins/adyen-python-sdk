
# Bill Desk

*This model accepts additional fields of type Any.*

## Structure

`BillDesk`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `issuer` | `str` | Required | The issuer id of the shopper's selected bank. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type121`](../../doc/models/type-121.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bill_desk import BillDesk
from adyen.models.type_121 import Type121

bill_desk = BillDesk(
    issuer='issuer6',
    mtype=Type121.BILLDESK_ONLINE,
    checkout_attempt_id='checkoutAttemptId2',
    sdk_data='sdkData4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

