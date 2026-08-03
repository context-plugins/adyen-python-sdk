
# Masterpass

*This model accepts additional fields of type Any.*

## Structure

`Masterpass`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `funding_source` | [`FundingSource`](../../doc/models/funding-source.md) | Optional | - |
| `masterpass_transaction_id` | `str` | Required | The Masterpass transaction ID. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type35`](../../doc/models/type-35.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.funding_source import FundingSource
from adyen.models.masterpass import Masterpass
from adyen.models.type_35 import Type35

masterpass = Masterpass(
    masterpass_transaction_id='masterpassTransactionId6',
    checkout_attempt_id='checkoutAttemptId8',
    funding_source=FundingSource.DEBIT,
    sdk_data='sdkData8',
    mtype=Type35.MASTERPASS,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

