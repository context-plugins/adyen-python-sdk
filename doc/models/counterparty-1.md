
# Counterparty 1

Contains information about the party that receives the payment funds.

*This model accepts additional fields of type Any.*

## Structure

`Counterparty1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder` | [`AccountHolder`](../../doc/models/account-holder.md) | Required | - |
| `account_identification` | [`AccountIdentification1`](../../doc/models/account-identification-1.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_holder import AccountHolder
from adyen.models.account_identification_1 import AccountIdentification1
from adyen.models.counterparty_1 import Counterparty1

counterparty_1 = Counterparty1(
    account_holder=AccountHolder(
        full_name='John Doe',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    account_identification=AccountIdentification1(
        mtype='AccountIdentification1',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

