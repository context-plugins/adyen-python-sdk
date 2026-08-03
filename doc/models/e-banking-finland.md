
# E Banking Finland

*This model accepts additional fields of type Any.*

## Structure

`EBankingFinland`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `issuer` | `str` | Optional | The Ebanking Finland issuer value of the shopper's selected bank. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type60`](../../doc/models/type-60.md) | Required | **ebanking_FI** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.e_banking_finland import EBankingFinland
from adyen.models.type_60 import Type60

e_banking_finland = EBankingFinland(
    mtype=Type60.EBANKING_FI,
    checkout_attempt_id='checkoutAttemptId8',
    issuer='issuer2',
    sdk_data='sdkData8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

