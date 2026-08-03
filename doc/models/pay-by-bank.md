
# Pay by Bank

*This model accepts additional fields of type Any.*

## Structure

`PayByBank`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `issuer` | `str` | Optional | The PayByBank issuer value of the shopper's selected bank. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type75`](../../doc/models/type-75.md) | Required | **paybybank** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.pay_by_bank import PayByBank
from adyen.models.type_75 import Type75

pay_by_bank = PayByBank(
    mtype=Type75.PAYBYBANK,
    checkout_attempt_id='checkoutAttemptId6',
    issuer='issuer0',
    sdk_data='sdkData0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

