
# Mol Pay

*This model accepts additional fields of type Any.*

## Structure

`MolPay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `issuer` | `str` | Required | The shopper's bank. Specify this with the issuer value that corresponds to this bank. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type38`](../../doc/models/type-38.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.mol_pay import MolPay
from adyen.models.type_38 import Type38

mol_pay = MolPay(
    issuer='issuer6',
    mtype=Type38.MOLPAY_EBANKING_FPX_MY,
    checkout_attempt_id='checkoutAttemptId2',
    sdk_data='sdkData4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

